
def select_data(connection,query):
    with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result

def change_data(connection,query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()