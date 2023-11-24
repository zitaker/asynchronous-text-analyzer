# import asyncio
# import json
# import aioredis
# # import pydantic
#
# from constants import BOOKS
# from datetime import datetime
# from pydantic import BaseModel, ValidationError
#
#
# class MyModel(BaseModel):
#     datetime: str
#     title: str
#     text: str
#     # text: str = Field(alias='ee')
#
# host = '127.0.0.1'
# port = 6379
#
# async def process_all_redis_data(host, port):
#     reader, writer = await asyncio.open_connection(host, port)
#     # print(reader)
#     data = await reader.read(100)  # Чтение 100 байт данных
#     print(data.decode())
#     writer.close()
#     await writer.wait_closed()
#
#
# if __name__ == '__main__':
#     asyncio.run(process_all_redis_data(host, port))
#
#
#
# # ################################################
# def dictionary(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         file_contents = file.read()
#
#     list_books = file_contents.split('\n\n\n\n\n\n')
#
#     result_dict = []
#     for elems in list_books:
#
#         lines = elems.split('\n')
#
#         title1 = lines[0].strip()
#         title = title1.replace('\ufeff', '')
#
#         body2 = '\n'.join(lines[1:]).strip()
#         body1 = body2.replace('\xa0', ' ')
#         body = body1.replace('\n', ' ')
#
#         data = {"title": title, "text": body}
#
#         result_dict.append(data)
#     return result_dict
#
#
# def date_time():
#     current_time = datetime.now()
#     formatted_time = current_time.strftime("%d.%m.%Y %H:%M:%S.%f")[:-3]
#     return formatted_time
#
#
# async def send_data(host, port, data):
#     reader, writer = await asyncio.open_connection(host, port)
#     print('отправка', data)
#
#     writer.write(json.dumps(data).encode())
#     await writer.drain()
#     writer.close()
#     await writer.wait_closed()
#
#
#
#
# async def data_preparation(host, port, data, interval=3):
#     for elem_dict in data:
#         dict_time = {"datetime": date_time()}
#         dictionary = {**dict_time, **elem_dict}
#         data_to_send = json.dumps(dictionary, ensure_ascii=False)
#
#         await send_data(host, port, data_to_send)
#         await process_all_redis_data(host, port)
#         await asyncio.sleep(interval)
#
#
# async def broker_message():
#     server_host = '127.0.0.1'
#     server_port = 6379
#     # data_to_send = dictionary(BOOKS)
#     data_to_send = [{'title': 'qwerty', 'text': 'qwe erett sergerg ergh'}, {'title': 'qwerty', 'text': 'qwe erett sergerg ergh'}]
#
#     await data_preparation(server_host, server_port, data_to_send)
#
# if __name__ == '__main__':
#     asyncio.run(broker_message())

import redis
r = redis.Redis()
r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
# True

print(r.get("Bahamas"))
# b'Nassau'
