import pytest

from fastapi.testclient import TestClient
from server import app
import insert_data


client = TestClient(app)


def test_get_by_trainer():
    res = client.get("/trainers/Drasna/pokemons")
    trainer_pokemons = res.json()
    assert res.status_code == 200
    assert ["wartortle", "caterpie", "beedrill", "arbok",
            "clefairy", "wigglytuff", "persian",
            "growlithe", "machamp", "golem", "dodrio",
            "hypno", "cubone", "eevee", "kabutops"] == trainer_pokemons


def test_delete_trainer_pokemon():
    insert_data.insert_pokemon_trainer(3, "Whitney")
    whitneys_pokemons_req = client.get("/trainers/Whitney/pokemons")
    assert whitneys_pokemons_req.status_code == 200
    whitneys_pokemons_req_body = whitneys_pokemons_req.json()
    assert 'venusaur' in whitneys_pokemons_req_body

    del_venusaur_req = client.delete("/trainers/Whitney/pokemons/venusaur")
    assert del_venusaur_req.status_code == 204

    whitneys_pokemons_req2 = client.get("/trainers/Whitney/pokemons")
    assert whitneys_pokemons_req2.status_code == 200
    whitneys_pokemons_req_body2 = whitneys_pokemons_req2.json()
    assert 'venusaur' not in whitneys_pokemons_req_body2
