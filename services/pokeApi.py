import requests
import json

async def get_pokemon_evolution_chain(pokemon_name):
    pokemon_data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    species_url = pokemon_data.json()["species"]["url"]
    pokemon_species = requests.get(species_url)
    evolution_url = pokemon_species.json()["evolution_chain"]["url"]
    pokemon_evolution_chain = requests.get(evolution_url)

    return pokemon_evolution_chain.json()["chain"]


async def get_next_evolution(pokemon_name):
    evolution_chain = await get_pokemon_evolution_chain(pokemon_name)
    pokemon = evolution_chain["species"]["name"]

    while pokemon != pokemon_name and len(evolution_chain["evolves_to"]) != 0:
        evolution_chain = evolution_chain["evolves_to"]
        pokemon = evolution_chain[0]["species"]["name"]



    return evolution_chain[0]["evolves_to"][0]["species"]["name"] or pokemon
