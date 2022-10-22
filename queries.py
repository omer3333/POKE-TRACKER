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

def get_heaviest_pokemon():
    try:
        with connection.cursor() as cursor:
            query = "SELECT name FROM pokemon WHERE MAX(weight)"
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except:
        print("Error")

def find_by_type(pokemon_type):
    try:
        with connection.cursor() as cursor:
            query = f"SELECT name FROM pokemon WHERE type={pokemon_type}"
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except:
        print("Error")

def find_owners(pokemon_name):
    try:
        with connection.cursor() as cursor:
            query = f"SELECT trainer_name FROM pokemon AS p ,pokemon_trainer AS pt WHERE p.id = pt.pokemon_id AND p.name ={pokemon_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except:
        print("Error")

def find_roster(trainer_name):
    try:
        with connection.cursor() as cursor:
            query = f"SELECT name FROM pokemon AS p ,pokemon_trainer AS pt WHERE p.id=pt.pokemon_id AND pt.trainer_name ={trainer_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except:
        print("Error")

def most_owned_pokemon():
    try:
        with connection.cursor() as cursor:
            query = f"SELECT name FROM pokemon AS p ,pokemon_trainer AS pt WHERE p.id=pt.pokemon_id AND pt.trainer_name ={trainer_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except:
        print("Error")