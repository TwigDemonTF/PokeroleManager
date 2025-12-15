def setup_game(client):
    client.post("/register", json={
        "username": "gm",
        "password": "pw"
    })

    r = client.post("/game", json={
        "name": "Test Game"
    })

    assert r.status_code == 201
    return r.json["gameId"]

def setup_base_pokemon(client):
    r = client.post("/basePokemon", json={
        "Name": "Squirtle",
        "BaseHealth": 20,
        "PrimaryType": "WATER",
        "Strength": 1,
        "StrengthPotential": 5
    })
    return r.json["pokemonId"]


def test_create_game_pokemon(client):
    game_id = setup_game(client)
    base_id = setup_base_pokemon(client)

    res = client.post("/gamePokemon", json={
        "gameId": game_id,
        "basePokemonId": base_id,
        "name": "Blue",
        "level": 5,
        "Guid": "ABC123"
    })

    assert res.status_code == 201
    assert "pokemonId" in res.json
