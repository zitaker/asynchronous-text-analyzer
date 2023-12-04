import psycopg2
import os
import json
# import asyncio


# async def taking_from_db():
def taking_from_db():
    DATABASE_URL = os.getenv('DATABASE_URL')
    conn = psycopg2.connect(DATABASE_URL)

    """
    query = value(datetime), value(title), value(x_avg_count_in_line),
    1) datetime = первое значение datetime по title, так же first_title_datetime.
    2) title = title без повторений.
    3) x_avg_count_in_line = сумма count_x / количество одинаковых title.
    """
    try:
        query = ("WITH FirstTitleDateTime AS (SELECT title, MIN(datetime) AS min_datetime FROM book GROUP BY title)"
                         "SELECT ftd.min_datetime AS first_title_datetime, b.title, ROUND(SUM(b.count_x) / COUNT(b.title), 3)"
                         "AS x_avg_count_in_line FROM book b JOIN FirstTitleDateTime ftd ON b.title = ftd.title GROUP BY b.title,"
                         "ftd.min_datetime;")

        with conn.cursor() as curs:
            curs.execute(query)

            result = []
            for elem in curs.fetchall():
                dictionary = {"datetime": elem[0], "title": elem[1], "x_avg_count_in_line": float(elem[2])}
                json_data = json.dumps(dictionary, ensure_ascii=False)
                result.append(json_data)

        curs.close()
        conn.close()
        return result
    except:
        print('Can`t establish connection to database')


if __name__ == '__main__':
    # asyncio.run(taking_from_db())
    taking_from_db()
