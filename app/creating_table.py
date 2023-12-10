import psycopg2
import os
import asyncio

from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


async def creating_table():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()

        # query = ("DROP TABLE IF EXISTS book;")
        query = ("CREATE TABLE IF NOT EXISTS book "
                 "(datetime VARCHAR(50) NOT NULL, "
                 "title VARCHAR(255) NOT NULL, "
                 "count_x NUMERIC);")

        with conn.cursor() as curs:
            curs.execute(query)

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        return {'error': f'{str(e)}'}


if __name__ == '__main__':
    asyncio.run(creating_table())
