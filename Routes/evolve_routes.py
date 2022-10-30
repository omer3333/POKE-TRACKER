
from unicodedata import name
from fastapi import Request
from fastapi import APIRouter
from pymysql import IntegrityError
import requests
from data_access import pokemon_queries, trainer_queries
from services import pokeApi
from fastapi import HTTPException
from insert_data import *


router = APIRouter(prefix="/evolve")


@router.put("/{trainer_name}/pokemons/{pokemon_name}", status_code=201)
async def evolve_pokemon(trainer_name,pokemon_name):
    try:
        evolved_to = await pokeApi.get_next_evolution(pokemon_name)
        pokemon_id = pokemon_queries.get_pokemon(evolved_to)[0]["id"]
        
        trainer_queries.delete_pokemon_from_trainer(trainer_name,pokemon_name)
        insert_pokemon_trainer(pokemon_id, trainer_name)

        return evolved_to

    except ValueError as e:
        raise HTTPException(status_code=400, detail=e.args[0])
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=e.args)
    except Exception as e:
        raise HTTPException(status_code=404,detail=e.args[0])
    except:
        raise HTTPException(status_code=500, detail="something went wrong")
