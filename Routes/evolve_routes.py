
from fastapi import APIRouter
from pymysql import IntegrityError
from ..services.pokemon import pokemon
from ..services.trainer import trainer
from ..services.pokeApi import *
from fastapi import HTTPException
from db.data_setup import *

router = APIRouter(prefix="/evolve")


@router.put("/{trainer_name}/pokemons/{pokemon_name}", status_code=201)
async def evolve_pokemon(trainer_name,pokemon_name):
    try:
        evolved_to = await get_next_evolution(pokemon_name)
        pokemon_id = pokemon.get_pokemon(evolved_to)[0]["id"]
        
        trainer.delete_pokemon_from_trainer(trainer_name,pokemon_name)
        trainer.insert_pokemon_trainer(pokemon_id, trainer_name)

        return evolved_to

    except ValueError as e:
        raise HTTPException(status_code=400, detail=e.args[0])
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=e.args)
    except Exception as e:
        raise HTTPException(status_code=404,detail=e.args[0])
    except:
        raise HTTPException(status_code=500, detail="something went wrong")
