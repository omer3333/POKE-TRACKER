
from fastapi import APIRouter, Request
import requests
from ..services.pokemon import pokemon


router = APIRouter(prefix="/pokemons")

# the actual path is /pokemons/{id}/trainers


@router.get("/{pokemon_name}/trainers", status_code=200)
async def get_trainers_of_pokemon(pokemon_name):
    return pokemon.find_owners(pokemon_name)


@router.get("/{pokemon_name}", status_code=200)
async def get_pokemon_types(pokemon_name):
    res = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    type_names_array = res.json()["types"]
    types = [item['type']['name'] for item in type_names_array]
    pokemon = pokemon.get_pokemon(pokemon_name)
    if (pokemon):
        pokemon[0]['type'] = types
        pokemon_id = pokemon[0]['id']
        for type in types:
            pokemon.insert_type(type)
            pokemon.insert_pokemon_types(pokemon_id, type)
    return pokemon


@router.get("/type/{type}", status_code=200)
async def find_by_type(type):
    return pokemon.find_by_type(type)


@router.post("/", status_code=201)
async def add_pokemon(request: Request):
    body = request.json()
    pokemon.insert_pokemon(
        body.id, body.name, body.height, body.weight)
    for type in body.types:
        pokemon.insert_pokemon_types(body.id, type)
