import asyncio
import aioredis


async def handle(reader, writer):
    while True:
        data = await reader.read(100)
        if not data:
            break

        # message = data.decode()
        # addr = writer.get_extra_info('peername')
        # print(f"Received {message!r} from {addr!r}")

        # print(f"Send: {message!r}")
        writer.write(data)
        await writer.drain()

        # print("Closing the connection")
        writer.close()


async def main():
    server = await asyncio.start_server(
        handle, '127.0.0.1', 6379)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
