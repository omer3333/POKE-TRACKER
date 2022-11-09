import requests

class Evolve:
    def _get_pokemon_evolution_chain(self,pokemon_name:str) ->dict:
        try:
            species_url= requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}').json()["species"]["url"]
            evolution_url = requests.get(species_url).json()["evolution_chain"]["url"]
            pokemon_evolution_chain = requests.get(evolution_url).json()["chain"]

            return pokemon_evolution_chain
        except:
            raise ValueError("Pokemon name is incorrect")


    def get_next_evolution(self,pokemon_name:str)->str:
        evolution_chain =  self._get_pokemon_evolution_chain(pokemon_name)
        pokemon = evolution_chain["species"]["name"]

        while pokemon != pokemon_name and len(evolution_chain["evolves_to"]) != 0:
            evolution_chain = evolution_chain["evolves_to"][0]
            pokemon = evolution_chain["species"]["name"]

        if len(evolution_chain) == 0:
            raise ValueError("Pokemon cannot evolve!")

        return evolution_chain["evolves_to"][0]["species"]["name"] 

evovle = Evolve()