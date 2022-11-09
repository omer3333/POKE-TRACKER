
from fastapi import APIRouter, Request
import requests
from services import pokemon

router = APIRouter(prefix="/pokemons")

@router.get("/{pokemon_name}/trainers", status_code=200)
async def get_trainers_of_pokemon(pokemon_name:str):
    return pokemon.find_owners(pokemon_name)
#TODO: You are raising exceptions in the methods in service ("find_owners", "get_pokemon" and etc) and not catching them here
# Meaning the application will crush and not return anything.


@router.get("/{pokemon_name}", status_code=200)
def get_pokemon_types(pokemon_name:str)->list:
    res = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    type_names_array = res.json()["types"]
    types = [item['type']['name'] for item in type_names_array]
    #TODO: lines 17-20 should not be here in the controller, the logic should be in "services"
    pokemon_data = pokemon.get_pokemon(pokemon_name)
    if (pokemon_data):
        pokemon_data[0]['type'] = types
        pokemon_id = pokemon_data[0]['id']
        for type in types:
            #TODO: We are in "get_pokemon_types" why are we inserting types?
            pokemon.insert_type(type)
            pokemon.insert_pokemon_types(pokemon_id, type)
    return pokemon_data


@router.get("/types/{type}", status_code=200)
def find_by_type(type:str) ->list :
    return pokemon.find_by_type(type)


@router.post("/", status_code=201)
async def add_pokemon(request: Request)->None:
    #TODO: Also remove async and await
    body = await request.json()
    pokemon.insert_pokemon(
        body.id, body.name, body.height, body.weight)
    #TODO: Parameter validation, make sure "id", "name", "height" and "weight" exists before using them.
    for type in body.types:
        #TODO: Why are we inserting a new type? every new pokemon is a new type ither?
        pokemon.insert_pokemon_types(body.id, type)
