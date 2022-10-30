from .db_connection import connection

# get pokemon by trainer


def get_pokemon(trainer_name):
    try:
        with connection.cursor() as cursor:
            roster_query = f"select name from pokemon join pokemon_trainer on pokemon_trainer.pokemon_id=pokemon.id where pokemon_trainer.trainer_name='{trainer_name}'"
            cursor.execute(roster_query)
            result = cursor.fetchall()
            return ([item["name"] for item in result])

    except Exception as e:
        return e


def create_trainer(name, town):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT IGNORE into trainer(name, town) values('{name}','{town}')"
            cursor.execute(query)
            connection.commit()
    except Exception as e:
        return e


def get_trainer(name):
    try:
        with connection.cursor() as cursor:
            query = f"select * from trainer where name='{name}'"
            cursor.execute(query)
            result = cursor.fetchall()
            return result
            # return result[0] //need to be checked if something return, return result- if empty return empty array
    except Exception as e:
        return e


def delete_pokemon_from_trainer(trainer_name, pokemon_name):
    try:
        with connection.cursor() as cursor:
            delete_query = f"delete pt from pokemon_trainer as pt join pokemon on pokemon.id=pt.pokemon_id where pt.trainer_name='{trainer_name}' and pokemon.name='{pokemon_name}'"
            cursor.execute(delete_query)
            connection.commit()
    except Exception as e:
        return e


def update_trainer_city(trainer_name, town):
    try:
        with connection.cursor() as cursor:
            query = f"update trainer set town='{town}' where name='{trainer_name}'"
            cursor.execute(query)
            connection.commit()
    except Exception as e:
        print(e)
        return e
