
from unicodedata import name
from fastapi import Request
from fastapi import APIRouter
from ..services.trainer import trainer

router = APIRouter(prefix="/trainers")


@router.get("/{trainer_name}/pokemons", status_code=200)
async def get_pokemons_by_trainer(trainer_name):
    return trainer.get_pokemon(trainer_name)


@router.post("/", status_code=201)
async def create_trainer(request: Request):
    body = await request.json()
    trainer.create_trainer(body["name"], body["town"])
    return trainer.get_trainer(body["name"])


@router.delete("/{trainer_name}/pokemons/{pokemon_name}", status_code=204)
async def delete_pokemon_from_trainer(trainer_name, pokemon_name):
    return trainer.delete_pokemon_from_trainer(trainer_name, pokemon_name)


@router.put("/{trainer_name}", status_code=201)
async def update_city(trainer_name, requset: Request):
    body = await requset.json()
    trainer.update_trainer_city(trainer_name, body["town"])
    return trainer.get_trainer(trainer_name)
