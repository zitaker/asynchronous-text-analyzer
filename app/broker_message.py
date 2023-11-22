import asyncio
import json

from constants import BOOKS
from datetime import datetime


def dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()

    list_books = file_contents.split('\n\n\n\n\n\n')

    result_dict = []
    for elems in list_books:

        lines = elems.split('\n')

        title1 = lines[0].strip()
        title = title1.replace('\ufeff', '')

        body2 = '\n'.join(lines[1:]).strip()
        body1 = body2.replace('\xa0', ' ')
        body = body1.replace('\n', ' ')

        data = {"title": title, "text": body}

        result_dict.append(data)
    return result_dict


def date_time():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%d.%m.%Y %H:%M:%S.%f")[:-3]
    return formatted_time


async def send_data(host, port, data):
    reader, writer = await asyncio.open_connection(host, port)
    print(data)
    writer.write(json.dumps(data).encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def send_data_periodically(host, port, data, interval=3):
    for elem_dict in data:
        dict1 = {"datetime": date_time()}
        dict2 = {**dict1, **elem_dict}
        data_to_send = json.dumps(dict2, ensure_ascii=False)

        await send_data(host, port, data_to_send)
        await asyncio.sleep(interval)


async def main():
    server_host = '127.0.0.1'
    server_port = 6379
    data_to_send = dictionary(BOOKS)

    await send_data_periodically(server_host, server_port, data_to_send)

if __name__ == '__main__':
    asyncio.run(main())