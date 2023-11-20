import asyncio
import json


async def send_data(host, port, data):
    reader, writer = await asyncio.open_connection(host, port)

    print(f'Sending data: {data!r}')
    writer.write(json.dumps(data).encode())
    await writer.drain()

    print('Data sent, waiting for response...')
    response = await reader.read(100)
    print(f'Received response: {response.decode()!r}')

    print('Closing the connection')
    writer.close()
    await writer.wait_closed()

async def send_data_periodically(host, port, data, interval=3):
    while True:
        await send_data(host, port, data)
        await asyncio.sleep(interval)

async def main():
    server_host = '127.0.0.1'
    server_port = 6379

    data_to_send = {"key": "value"}

    # Отправка данных на сервер с интервалом в 3 секунды
    await send_data_periodically(server_host, server_port, data_to_send)

if __name__ == '__main__':
    asyncio.run(main())