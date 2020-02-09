import psycopg2
try:
    connection = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432")

    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT * FROM prompt_table;"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from prompt_table using cursor.fetchall")
    prompt_records = cursor.fetchall()

    print("print each row and it's column values")
    for row in prompt_records:
        print("id_prompt = ", row[0], )
        print("name = ", row[1])
        print("status = ", row[2])
        print("created = ", row[3], "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")