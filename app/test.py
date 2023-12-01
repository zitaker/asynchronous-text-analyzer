import psycopg2
import os
import asyncio

from broker_message import parse_from_broker_message
# from broker_message import load


async def sending_to_db():
    result = await parse_from_broker_message()
    if result:
        datetime, title, count_x = result
        print("datetime:", datetime)
        print("title:", title)
        print("count_x:", count_x)
    else:
        print("Error occurred during parsing.")

    DATABASE_URL = os.getenv('DATABASE_URL')
    conn = psycopg2.connect(DATABASE_URL)

    datetime_value = '44'
    title_value = 'ййя'
    count_x_value = 56

    try:
        # print('подключил SQL')
        query_sending_data = ("INSERT INTO book (datetime, title, count_x) "
                              "VALUES (%(datetime)s, %(title)s, %(count_x)s)")
        values = {
            'datetime': datetime_value,
            'title': title_value,
            'count_x': count_x_value
        }
        with conn.cursor() as curs:
            curs.execute(query_sending_data, values)
            conn.commit()
        conn.close()

    except:
        print('Can`t establish connection to database')


if __name__ == '__main__':
    asyncio.run(sending_to_db())
