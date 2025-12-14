# Test login

def test_login_success(client):
    client.post("/register", json={"username": "misty", "password": "togepi"})
    
    response = client.post("/masterLogin", json={
        "username": "misty",
        "password": "togepi"
    })

    assert response.status_code == 200
    assert "Welcome, misty!" in response.json["message"]


def test_login_wrong_password(client):
    client.post("/register", json={"username": "misty", "password": "togepi"})

    response = client.post("/masterLogin", json={
        "username": "misty",
        "password": "wrongpass"
    })

    assert response.status_code == 401
