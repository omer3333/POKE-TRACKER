# import json
# import pymysql
# import os

# pokemon_file = open("./pokemon_data.json")
# pokemon_data = json.load(pokemon_file)


# connection = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     db="poketracker",
#     charset="utf8",
#     cursorclass=pymysql.cursors.DictCursor
# )


# def insert_pokemon(id, name, height, weight):
#     with connection.cursor() as cursor:
#         query = f"INSERT IGNORE into pokemon(id, name, height, weight) values({id}, '{name}', {height},{weight})"
#         cursor.execute(query)
#         connection.commit()


# def insert_trainer(name, town):
#     with connection.cursor() as cursor:
#         query = f"INSERT IGNORE into trainer(name, town) values('{name}','{town}')"
#         cursor.execute(query)
#         connection.commit()
 

# def insert_type(name):
#     with connection.cursor() as cursor:
#         query = f"INSERT IGNORE into types(name) values('{name}')"
#         cursor.execute(query)
#         connection.commit()

# def insert_pokemon_types(pokemon_id, type_name):
#     with connection.cursor() as cursor:
#         query = f"INSERT into pokemon_types(pokemon_id, type_name) values({pokemon_id},'{type_name}')"
#         cursor.execute(query)
#         connection.commit()

# def insert_pokemon_trainer(pokemon_id, trainer_name):
#     with connection.cursor() as cursor:
#         query = f"INSERT into pokemon_trainer(pokemon_id, trainer_name) values({pokemon_id}, '{trainer_name}')"
#         cursor.execute(query)
#         connection.commit()

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


# # insert_all("pokemon_data.json")
