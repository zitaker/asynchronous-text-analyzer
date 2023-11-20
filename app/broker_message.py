import asyncio


async def send_data(host, port, data):
    reader, writer = await asyncio.open_connection(host, port)

    print(f'Sending data: {data!r}')
    writer.write(data.encode())
    await writer.drain()

    print('Data sent, waiting for response...')
    response = await reader.read(100)
    print(f'Received response: {response.decode()!r}')

    print('Closing the connection')
    writer.close()
    await writer.wait_closed()


async def main():
    server_host = '127.0.0.1'
    server_port = 6379

    # Отправка данных на сервер
    data_to_send = "Hello, server!"
    await send_data(server_host, server_port, data_to_send)

    # Получение данных с сервера
    data_to_send = "Requesting data from server"
    await send_data(server_host, server_port, data_to_send)

if __name__ == '__main__':
    asyncio.run(main())
