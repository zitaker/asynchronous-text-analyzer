import asyncio
import redis
import json
import psycopg2
import os

from constants import BOOKS
from datetime import datetime
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


class ModelDictionary(BaseModel):
    datetime: str
    title: str
    text: str


def get_list_of_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()

    list_books = file_contents.split('\n\n\n\n\n\n')

    list_dictionary = []
    for elems in list_books:

        lines = elems.split('\n')

        old_title = lines[0].strip()
        new_title = old_title.replace('\ufeff', '')

        oldest_body = '\n'.join(lines[1:]).strip()
        old_body = oldest_body.replace('\xa0', ' ')

        old_lines_body = old_body.splitlines()
        body_without_empty_lines = \
            [line for line in old_lines_body if line.strip()]
        for new_body in body_without_empty_lines:
            dictionary = {"title": new_title, "text": new_body}
            list_dictionary.append(dictionary)
    return list_dictionary


def get_datetime():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%d.%m.%Y %H:%M:%S.%f")[:-3]
    return formatted_time


async def send_message_to_the_broker(list_dictionary):
    for dictionary in list_dictionary:
        time_dictionary = {"datetime": get_datetime()}
        new_dictionary = {**time_dictionary, **dictionary}

        connection = redis.Redis()
        hash_key = 'hash_key'
        encoded_message = json.dumps(new_dictionary,
                                     ensure_ascii=False).encode('utf-8')
        connection.set(hash_key, encoded_message)

        await parse_broker_message()


def search_symbols_x(text):
    my_text = text.text
    search_char = 'х'
    count_x = my_text.upper().count(search_char.upper())
    return count_x


async def parse_broker_message():
    connection = redis.Redis()
    hash_key = 'hash_key'
    retrieved_message = connection.get(hash_key)
    decoded_message = json.loads(retrieved_message.decode('utf-8'))

    json_data = json.dumps(decoded_message, ensure_ascii=False)
    try:
        my_data = ModelDictionary.model_validate_json(json_data)

        datetime = my_data.datetime
        title = my_data.title
        count_x = search_symbols_x(my_data)

        await asyncio.sleep(3)
        await send_to_the_database(datetime, title, count_x)
    except Exception as e:
        return {'error': f'{str(e)}'}


async def send_to_the_database(datetime, title, count_x):
    datetime_value = datetime
    title_value = title
    count_x_value = count_x

    try:
        conn = psycopg2.connect(DATABASE_URL)
        query_sending_data = ("INSERT INTO book (datetime, title, count_x) "
                              "VALUES (%(datetime)s, %(title)s, %(count_x)s)")
        values = {
            'datetime': datetime_value,
            'title': title_value,
            'count_x': count_x_value
        }
        with conn.cursor() as curs:
            curs.execute(query_sending_data, values)
            conn.commit()
        curs.close()
        conn.close()
    except Exception as e:
        return {'Can`t establish connection to database': f'error: {str(e)}'}


async def load_data():
    await send_message_to_the_broker(get_list_of_dictionary(BOOKS))


if __name__ == '__main__':
    asyncio.run(load_data())
