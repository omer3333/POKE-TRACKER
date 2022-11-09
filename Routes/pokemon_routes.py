
from fastapi import APIRouter, Request
import requests
from services import pokemon

router = APIRouter(prefix="/pokemons")

@router.get("/{pokemon_name}/trainers", status_code=200)
async def get_trainers_of_pokemon(pokemon_name:str):
    return pokemon.find_owners(pokemon_name)


@router.get("/{pokemon_name}", status_code=200)
def get_pokemon_types(pokemon_name:str)->list:
    res = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    type_names_array = res.json()["types"]
    types = [item['type']['name'] for item in type_names_array]
    pokemon_data = pokemon.get_pokemon(pokemon_name)
    if (pokemon_data):
        pokemon_data[0]['type'] = types
        pokemon_id = pokemon_data[0]['id']
        for type in types:
            pokemon.insert_type(type)
            pokemon.insert_pokemon_types(pokemon_id, type)
    return pokemon_data


@router.get("/types/{type}", status_code=200)
def find_by_type(type:str) ->list :
    return pokemon.find_by_type(type)


@router.post("/", status_code=201)
async def add_pokemon(request: Request)->None:
    body = await request.json()
    pokemon.insert_pokemon(
        body.id, body.name, body.height, body.weight)
    for type in body.types:
        pokemon.insert_pokemon_types(body.id, type)
