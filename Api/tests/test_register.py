# Test registration

def test_register_success(client):
    response = client.post("/register", json={
        "username": "ash",
        "password": "pikachu"
    })

    assert response.status_code == 201
    assert response.json["message"] == "User registered successfully"


def test_register_duplicate_username(client):
    client.post("/register", json={"username": "ash", "password": "123"})
    response = client.post("/register", json={"username": "ash", "password": "456"})

    assert response.status_code == 409
    assert response.json["message"] == "Username already exists"
