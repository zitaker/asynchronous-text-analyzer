import asyncio
import redis
# import pydantic

from constants import BOOKS
from datetime import datetime
# from pydantic import BaseModel, ValidationError


# class MyModel(BaseModel):
#     datetime: str
#     title: str
#     text: str
#     # text: str = Field(alias='ee')


# ################################################



def list_of_dictionary(file_path):
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
        new_body = old_body.replace('\n', ' ')

        dictionary = {"title": new_title, "text": new_body}

        list_dictionary.append(dictionary)
    return list_dictionary


def date_time():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%d.%m.%Y %H:%M:%S.%f")[:-3]
    return formatted_time


async def send_messages_to_the_broker(list_dictionary):
    for dictionary in list_dictionary:
        time_dictionary = {"datetime": date_time()}
        new_dictionary = {**time_dictionary, **dictionary}

        connection = redis.Redis()
        hash_key = 'hash_key'
        for field, value in new_dictionary.items():
            connection.hset(hash_key, field, value)

        await parse_from_broker_message()



test_data = [{'qwer': '11'}, {'qwer': '444'}]

async def parse_from_broker_message():
    connection = redis.Redis()
    message = connection.hgetall('hash_key')
    print(message)
    await asyncio.sleep(3)


async def main():
    # await send_data(list_of_dictionary(BOOKS))

    await send_messages_to_the_broker(list_of_dictionary(BOOKS))


if __name__ == '__main__':
    asyncio.run(main())
