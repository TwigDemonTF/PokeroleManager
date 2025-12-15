def test_create_base_pokemon(client):
    res = client.post("/basePokemon", json={
        "Name": "Bulbasaur",
        "BaseHealth": 20,
        "PrimaryType": "GRASS",
        "Strength": 2,
        "StrengthPotential": 5
    })

    assert res.status_code == 201
    assert "pokemonId" in res.json


def test_get_base_pokemon(client):
    client.post("/basePokemon", json={
        "Name": "Charmander",
        "BaseHealth": 18,
        "PrimaryType": "FIRE"
    })

    res = client.get("/basePokemon")
    assert res.status_code == 200
    assert any(p["name"] == "Charmander" for p in res.json)