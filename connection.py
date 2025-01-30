import pandas as pd
import pymysql

def connect_mysql():
    connection = pymysql.connect(
        user="root",
        host="localhost",
        database="StudentDB",
        password="654321"
    )

    cursor = connection.cursor()

    query = "SELECT * FROM StudentDB.student_info_1"
    cursor.execute(query)
    data = cursor.fetchall()

    df = pd.DataFrame(data)
    print(df)



connect_mysql()
