
from fastapi import APIRouter
from pymysql import IntegrityError
from services import pokemon
from services import trainer
from services import evovle
from fastapi import HTTPException
from db.data_setup import *

router = APIRouter(prefix="/evolve")

# TODO: remove "async" and "await" - we are waiting for the responses so there is no use for that. 

@router.put("/{trainer_name}/pokemons/{pokemon_name}", status_code=201)
async def evolve_pokemon(trainer_name:str,pokemon_name:str) -> str:
    try:
        evolved_to = await evovle.get_next_evolution(pokemon_name)
        pokemon_id = pokemon.get_pokemon(evolved_to)[0]["id"]
        # TODO: Can "get_pokemon" return None? if does validate the content before approaching it.
        
        trainer.delete_pokemon_from_trainer(trainer_name,pokemon_name)
        trainer.insert_pokemon_trainer(pokemon_id, trainer_name)

        return evolved_to

    except ValueError as e:
        raise HTTPException(status_code=400, detail=e.args[0])
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=e.args)
    except Exception as e:
        raise HTTPException(status_code=404,detail=e.args[0])

