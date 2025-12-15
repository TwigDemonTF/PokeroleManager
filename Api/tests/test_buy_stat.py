def test_buy_stat_requires_xp(client):
    res = client.post("/buyStat/TESTGAME/TESTGUID", json={
        "stat": "Strength"
    })

    assert res.status_code in (400, 404)