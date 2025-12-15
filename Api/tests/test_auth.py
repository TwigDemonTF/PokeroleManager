def test_register_user(client):
    res = client.post("/register", json={
        "username": "testuser",
        "password": "secret"
    })
    assert res.status_code == 201
    assert res.json["message"] == "User registered successfully"


def test_register_duplicate_user(client):
    client.post("/register", json={
        "username": "dup",
        "password": "secret"
    })

    res = client.post("/register", json={
        "username": "dup",
        "password": "secret"
    })

    assert res.status_code == 409


def test_master_login_success(client):
    client.post("/register", json={
        "username": "loginuser",
        "password": "pw"
    })

    res = client.post("/masterLogin", json={
        "username": "loginuser",
        "password": "pw"
    })

    assert res.status_code == 200
    assert "gameId" in res.json


def test_master_login_failure(client):
    res = client.post("/masterLogin", json={
        "username": "nope",
        "password": "wrong"
    })
    assert res.status_code == 401