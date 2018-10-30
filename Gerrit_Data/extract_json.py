import pymysql.cursors
import json

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='gerrit_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


try:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM people"
        cursor.execute(sql)
        result = cursor.fetchall()
        y = json.dumps(result)

        print(y)

        # for row in result:

        #     print(row["gerrit_id"])

        #     print(row["full_name"])   

        #     print(row["preferred_email"])   

        #     print(row["username"])   

        # print(result)
finally:
    connection.close()