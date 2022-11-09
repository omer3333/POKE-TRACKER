
from fastapi import Request
from fastapi import APIRouter
from services import trainer

router = APIRouter(prefix="/trainers")

@router.get("/{trainer_name}", status_code=200)
def get_trainer(trainer_name:str)->dict:
    return trainer.get_trainer(trainer_name)


@router.get("/{trainer_name}/pokemons", status_code=200)
def get_pokemons_by_trainer(trainer_name:str)->list:
    return trainer.get_pokemon(trainer_name)


@router.post("/", status_code=201)
async def create_trainer(request: Request) ->None:
    #TODO: Remove async and await
    body = await request.json()
    #TODO: Parameters validation
    trainer.create_trainer(body["name"], body["town"])
    return trainer.get_trainer(body["name"])


@router.delete("/{trainer_name}/pokemons/{pokemon_name}", status_code=204)
def delete_pokemon_from_trainer(trainer_name:str, pokemon_name:str)-> None:
    return trainer.delete_pokemon_from_trainer(trainer_name, pokemon_name)


@router.put("/{trainer_name}", status_code=201)
async def update_city(trainer_name:str, requset: Request) -> None:
    #TODO: Async and await
    body = await requset.json()
    trainer.update_trainer_city(trainer_name, body["town"])
    return trainer.get_trainer(trainer_name)
