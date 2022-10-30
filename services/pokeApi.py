import requests
import json

async def get_pokemon_evolution_chain(pokemon_name):
    species_url= requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}').json()["species"]["url"]
    evolution_url = requests.get(species_url).json()["evolution_chain"]["url"]
    pokemon_evolution_chain = requests.get(evolution_url).json()["chain"]

    return pokemon_evolution_chain


async def get_next_evolution(pokemon_name):
    evolution_chain = await get_pokemon_evolution_chain(pokemon_name)
    pokemon = evolution_chain["species"]["name"]

    while pokemon != pokemon_name and len(evolution_chain["evolves_to"]) != 0:
        evolution_chain = evolution_chain["evolves_to"][0]
        pokemon = evolution_chain["species"]["name"]

    return pokemon if len(evolution_chain) == 0 else evolution_chain["evolves_to"][0]["species"]["name"] 