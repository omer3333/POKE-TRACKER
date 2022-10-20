import json
import pymysql


pokemon_file = open("pokemon_data.json")
pokemon_data = json.load(pokemon_file)


connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poketracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def insert_pokemon(id, name, height, weight):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT into pokemon(id, name, height, weight) values({id}, '{name}', {height},{weight})"
            cursor.execute(query)
            connection.commit()

    except:
        print("Error")


def insert_trainer(name, town):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT into trainer(name, town) values('{name}','{town}')"
            cursor.execute(query)
            connection.commit()

    except:
        print("Error")


def insert_type(name):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT into types(name) values('{name}')"
            cursor.execute(query)
            connection.commit()

    except:
        print("Error")


# def insert_pokemon_type(id, name, type_name, ):
#     try:
#         with connection.cursor() as cursor:
#             query = f"INSERT into types(name) values('{name}')"
#             cursor.execute(query)
#             connection.commit()

#     except:
#         print("Error")


# insert_pokemon(1, "balbazor", 100, 60)
# insert_trainer("ash", "tel-aviv")
insert_type("fire")

def setup_db(data):
    trainers = {}
    types = {}
    for pokemon in data:
        insert_pokemon(pokemon["id"],pokemon["name"],pokemon["height"],pokemon["weight"])
        insert_pokemon_type()
        for trainer in pokemon["ownedBy"]:
            unique_key = trainer["name"]+trainer["town"]
            trainers[unique_key] = trainer
            types.add(pokemon["type"])

    for trainer in trainers:
        insert_trainer(trainer["name"],trainer["town"])
    for type in types:
        insert_type(type)
