import psycopg2
import os
import asyncio

from broker_message import date_time


async def sending_to_db():
    DATABASE_URL = os.getenv('DATABASE_URL')
    conn = psycopg2.connect(DATABASE_URL)

    try:
        average_value = ("SELECT ROUND(SUM(count_x) / NULLIF(COUNT(count_x), 0), 3)"
                         "AS division_result FROM book;")

        with conn.cursor() as curs:
            curs.execute(average_value)
            result = curs.fetchone()[0]
            print(result)

        conn.close()
    except:
        print('Can`t establish connection to database')

if __name__ == '__main__':
    asyncio.run(sending_to_db())
