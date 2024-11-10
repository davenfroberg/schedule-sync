import pymysql
import os

"""
This file contains the functions to connect to the database and run a SQL query in the database.
"""

def query(sql_query: str):
    connection = pymysql.connect(
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_DATABASE']
    )

    cursor = connection.cursor()
    cursor.execute(sql_query)

    results = cursor.fetchall()
    connection.commit()

    cursor.close()
    connection.close()

    return results
