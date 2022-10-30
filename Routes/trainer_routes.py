
from unicodedata import name
from fastapi import Request
from fastapi import APIRouter
import requests
from data_access import trainer_queries


router = APIRouter(prefix="/trainers")

# the actual path is /trainers/{trainer_name}/pokemons


@router.get("/{trainer_name}/pokemons", status_code=200)
async def get_pokemons_by_trainer(trainer_name):
    return trainer_queries.get_pokemon(trainer_name)


@router.post("/", status_code=201)
async def create_trainer(request: Request):
    body = await request.json()
    trainer_queries.create_trainer(body["name"], body["town"])
    return trainer_queries.get_trainer(body["name"])


@router.delete("/{trainer_name}/pokemons/{pokemon_name}", status_code=204)
async def delete_pokemon_from_trainer(trainer_name, pokemon_name):
    return trainer_queries.delete_pokemon_from_trainer(trainer_name, pokemon_name)


@router.put("/{trainer_name}", status_code=201)
async def update_city(trainer_name, requset: Request):
    body = await requset.json()
    trainer_queries.update_trainer_city(trainer_name, body["town"])
    return trainer_queries.get_trainer(trainer_name)


