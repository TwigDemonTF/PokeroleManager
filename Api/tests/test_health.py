def test_update_health_sets_fainted(client):
    # You would normally reuse helpers to create game + pokemon
    # Example assumes pokemon already exists with Guid "TEST1"

    res = client.post("/updateHealth", json={
        "gameId": "TESTGAME",
        "guid": "TEST1",
        "health": 0
    })

    if res.status_code == 200:
        assert res.json["pokemon"]["status"] == "FAINTED"
