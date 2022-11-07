from ..db.config import connection
from ..db.utils import *
from ..db.trainer_queries import *

class Trainer:
    def get_pokemon(trainer_name):
        try:
            data = select_data(connection,SELECT_POKEMON_BY_TRAINER.format(trainer_name=trainer_name))
            return ([item["name"] for item in data])
        except:
            raise KeyError("trainer name does not exist")


    def create_trainer(name, town):
        try:
            change_data(connection,INSERT_TRAINER.format(name=name,town=town))
        except:
            raise Exception("could not create trainer")


    def get_trainer(name):
        try:
            return select_data(connection,SELECT_TRAINER.format(name=name))
        except:
            raise KeyError("trainer name does not exist")

    def insert_pokemon_trainer(pokemon_id, trainer_name):
        change_data(connection,INSERT_POKEMON_TO_TRAINER.format(pokemon_id=pokemon_id,trainer_name=trainer_name))

    def delete_pokemon_from_trainer(trainer_name, pokemon_name):
        try:
            change_data(connection,DELETE_POKEMON_FROM_TRAINER(trainer_name=trainer_name,pokemon_name=pokemon_name))
        except Exception as e:
            raise e

    def update_trainer_city(trainer_name, town):
        try:
            change_data(connection,UPDATE_TRAINER_CITY.format(trainer_name=trainer_name,town=town))
        except:
            raise KeyError("Trainer name is incorrect")


trainer = Trainer()