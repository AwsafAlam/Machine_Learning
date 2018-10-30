import pymysql.cursors
import json

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='gerrit_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
def search(req_id):
    for p in request_detail:
        if p['request_id'] == req_id:
            return p

try:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()

    
    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT * FROM inline_comments"
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     inline_comments = json.dumps(result , default=str)
        
    #     # print(y)

    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT * FROM patches"
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     patches = json.dumps(result , default=str)

    #     # print(y)

    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT * FROM patch_details"
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     patch_details = json.dumps(result , default=str)

    #     # print(y)

    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT * FROM people"
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     people = json.dumps(result , default=str)

    
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM requests"
        cursor.execute(sql)
        result = cursor.fetchall()
        tmp = {}
        for row in result:
            tmp = row
            tmp["last_updated_on"] = str(row["last_updated_on"])
            tmp["created"] = str(row["created"])

        requests = json.dumps(tmp)

        # print(y)


    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM request_detail"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            row["created"] = str(row["created"])
            row["updated"] = str(row["updated"])

        
        request_detail = json.dumps(result)

        # print(y)

    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT * FROM reviews"
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     reviews = json.dumps(result , default=str)

        # print(y)

    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT * FROM review_comments"
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     review_comments = json.dumps(result , default=str)

    # print(requests)
    # print(people)

    finalJSON = {}

    for row in requests:
        finalJSON["request_id"] = {
            "change_id" : search(row["request_id"])
        } 

    y = json.dumps(finalJSON)
    print(y)

finally:
    connection.close()


