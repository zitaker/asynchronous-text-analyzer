import asyncio
import redis


async def main():
    connection = redis.Redis()
    hash_key = 'hash_key1'

    translation_data = {
        'hello': 'привет',
        'world': 'мир',
        'example': 'пример'
    }

    connection.hset(hash_key, translation_data)


    english_word = 'hello'
    russian_translation = connection.hget(hash_key, english_word)
    print(f"{english_word}: {russian_translation}")


if __name__ == "__main__":
    asyncio.run(main())
