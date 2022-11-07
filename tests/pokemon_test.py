from fastapi.testclient import TestClient
from server import app


client = TestClient(app)


def test_pokemon_type():
    res = client.get("/pokemons/type/normal")
    normal_type = res.json()
    assert res.status_code == 200
    assert "eevee" in normal_type


def get_owners_of_pokemon():
    res = client.get("pokemons/charmander/trainers")
    trainers = res.json()
    assert res.status_code == 200
    assert ["Giovanni", "Jasmine", "Whitney"] == trainers
