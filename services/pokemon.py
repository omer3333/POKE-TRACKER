from ..db.config import connection
from ..db.utils import *
from ..db.pokemon_queries import *

class Pokemon:
    def get_heaviest_pokemon():
        try:
            return select_data(connection,SELECT_HEVIEST_POKEMON)
        except:
            raise Exception("Couldn't find heviest pokemon")

    def find_by_type(type):
        try:
            data = select_data(connection,SELECT_BY_TYPE.format(type=type))
            return ([item["name"] for item in data])
        except:
            raise KeyError("pokemon type is incorrect")


    def find_owners(pokemon_name):
        try:
            data = select_data(connection,SELECT_OWNER_BY_POKEMON.format(pokemon_name=pokemon_name))
            return ([owner["trainer_name"] for owner in data])
        except:
            raise KeyError("pokemon name does not exist")

    def most_owned_pokemon():
        try:
            return select_data(connection,SELECT_MOST_OWEND_POKEMON)
        except:
            raise Exception("Couldn't find most owned pokekmon")

    def get_pokemon(name):
        try:
            return select_data(connection,SELECT_POKEMON.format(name=name))
        except:
            raise KeyError("pokemon name does not exist")

    def insert_pokemon_types(pokemon_id, type_name):
        change_data(connection,INSERT_POKEMON_TYPES.format(pokemon_id=pokemon_id,type_name=type_name))

    def insert_type(name):
        change_data(connection,INSERT_TYPE.format(name=name))

    def insert_pokemon(id, name, height, weight):
        change_data(connection,INSERT_POKEMON.format(id=id,name=name,height=height,weight=weight))


pokemon = Pokemon()