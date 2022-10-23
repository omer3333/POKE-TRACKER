from distutils.log import error
from .db_connection import connection


def heaviest_pokemon():
    try:
        with connection.cursor() as cursor:
            heaviest_query = f"Select * from pokemon where weight = (select MAX(weight) from pokemon)"
            cursor.execute(heaviest_query)
            result = cursor.fetchall()
            return result

    except error as e:
        return e


def find_by_type(type):
    try:
        with connection.cursor() as cursor:
            byType_query = f"select name from pokemon join pokemon_types on pokemon_types.pokemon_id=pokemon.id WHERE pokemon_types.type_name='{type}'"
            cursor.execute(byType_query)
            result = cursor.fetchall()
            return ([item["name"] for item in result])
            # return [{"name": item["name"], "type": type} for item in result]

    except error as e:
        return e


def find_owners(pokemon_name):
    try:
        with connection.cursor() as cursor:
            findOwners_query = f"select trainer_name from pokemon_trainer join pokemon on pokemon.id= pokemon_trainer.pokemon_id where pokemon.name='{pokemon_name}'"
            cursor.execute(findOwners_query)
            result = cursor.fetchall()
            return ([owner["trainer_name"] for owner in result])

    except error as e:
        return e


def most_owned_pokemon():
    try:
        with connection.cursor() as cursor:
            most_owned_query = f"select name, COUNT(*) as val from pokemon join pokemon_trainer on pokemon_trainer.pokemon_id=pokemon.id GROUP BY pokemon.name ORDER by val DESC limit 2"
            cursor.execute(most_owned_query)
            result = cursor.fetchall()
            return ([item["name"] for item in result])

    except error as e:
        return e


def get_pokemon(name):
    try:
        with connection.cursor() as cursor:
            get_query = f"select * from pokemon where name='{name}'"
            cursor.execute(get_query)
            result = cursor.fetchall()
            return result

    except error as e:
        return e


def insert_pokemon_types(pokemon_id, type_name):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT into pokemon_types(pokemon_id, type_name) values({pokemon_id},'{type_name}')"
            print(query)
            cursor.execute(query)
            connection.commit()

    except Exception as e:
        print(e)


def insert_type(name):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT IGNORE into types(name) values('{name}')"
            cursor.execute(query)
            connection.commit()

    except:
        print("Error")

    # print(find_owners("pikachu"))
# print(find_roster("Loga"))
print(most_owned_pokemon())
