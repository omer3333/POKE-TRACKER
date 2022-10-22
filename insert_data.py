from cmath import e, polar
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
            query = f"INSERT IGNORE into pokemon(id, name, height, weight) values({id}, '{name}', {height},{weight})"
            cursor.execute(query)
            connection.commit()

    except:
        print("Error")


def insert_trainer(name, town):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT IGNORE into trainer(name, town) values('{name}','{town}')"
            cursor.execute(query)
            connection.commit()
    except:
        print("Error")


def insert_type(name):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT IGNORE into types(name) values('{name}')"
            cursor.execute(query)
            connection.commit()

    except:
        print("Error")


def insert_pokemon_types(pokemon_id, type_name):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT into pokemon_types(pokemon_id, type_name) values({pokemon_id},'{type_name}')"
            print(query)
            cursor.execute(query)
            connection.commit()

    except Exception as e:
        print(e)


# insert_pokemon(1, "balbazor", 100, 60)
# insert_trainer("ash", "tel-aviv")
insert_type("fire")

# def setup_db(data):
#     trainers = {}
#     types = {}
#     for pokemon in data:
#         insert_pokemon(pokemon["id"],pokemon["name"],pokemon["height"],pokemon["weight"])
#         insert_pokemon_type()
#         for trainer in pokemon["ownedBy"]:
#             unique_key = trainer["name"]+trainer["town"]
#             trainers[unique_key] = trainer
#             types.add(pokemon["type"])

#     for trainer in trainers:
#         insert_trainer(trainer["name"],trainer["town"])
#     for type in types:
#         insert_type(type)
def insert_pokemon_trainer(pokemon_id, trainer_name):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT IGNORE into pokemon_trainer(pokemon_id, trainer_name) values({pokemon_id}, '{trainer_name}')"
            print(query)
            cursor.execute(query)
            connection.commit()

    except Exception as e:
        print(e)


# def insert_all(json_file):
#     with open(json_file) as f:
#         data = json.loads(f.read())
#         for pokemon in data:
#             insert_pokemon(pokemon["id"], pokemon["name"],
#                            pokemon["height"], pokemon["weight"])
#             insert_type(pokemon["type"])
#             insert_pokemon_types(pokemon["id"], pokemon["type"])

#             for owner in pokemon["ownedBy"]:
#                 insert_trainer(owner["name"], owner["town"])
#                 insert_pokemon_trainer(pokemon["id"], owner["name"])


# insert_pokemon(2, "balbazor", 100, 60)
# insert_trainer("bla", "tel-aviv")
# insert_type("water")
# insert_pokemon_types(1, "water")
# insert_pokemon(3, "charizard", 200, 100)
# insert_pokemon_trainer(2, 'brook')
insert_all("pokemon_data.json")
