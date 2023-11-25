import asyncio
import json
import redis
# import aioredis
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

# class DataForPush:
#     def __init__(self):
#         self._dictionary = []
#
#     @property
#     def dictionary_to_send(self):
#         return self._dictionary.copy()
#
#     @dictionary_to_send.setter
#     def dictionary_to_send(self, new_dictionary):
#         self._dictionary = new_dictionary.copy()


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

# def qwerty(new_dictionary):
#     connection = redis.Redis()
#     hash_key = 'hash_key'
#     for field, value in new_dictionary.items():
#         connection.hset(hash_key, field, value)

async def send_data(list_dictionary):
    # reader, writer = await asyncio.open_connection(host, port)
    # print('отправка', data)
    #
    # writer.write(json.dumps(data).encode())
    # await writer.drain()
    # writer.close()
    # await writer.wait_closed()


    # obj = DataForPush()
    obj = []

    for dictionary in list_dictionary:
        # await asyncio.sleep(3)
        time_dictionary = {"datetime": date_time()}
        new_dictionary = {**time_dictionary, **dictionary}
        # data_to_send = json.dumps(new_dictionary, ensure_ascii=False)
            # for key, value in new_dictionary.items():
            #     obj[key] = value
        obj.append(new_dictionary)

    # print(obj)
    connection = redis.Redis()
    for i in obj:
        hash_key = 'hash_key'
        for field, value in i.items():
            connection.hset(hash_key, field, value)



test_data = [{'qwer': '11', 'asdf': '222'}, {'qaz': '444', 'wsx': '55'}]

async def main():
    # await send_data(list_of_dictionary(BOOKS))
    await send_data(test_data)
    connection = redis.Redis()
    print(connection.hgetall('hash_key'))
    # await asyncio.sleep(3)


if __name__ == '__main__':
    asyncio.run(main())


# connection = redis.Redis()

# hash_key = 'hash_key'

# data = {
#     "name": "John Doe",
#     "age": 30,
#     "email": "john.doe@example.com"
# }

# Отправка данных в Redis хеш
# for field, value in data.items():
#     connection.hset(hash_key, field, value)

# получение данных
# print(connection.hgetall('hash_key'))


