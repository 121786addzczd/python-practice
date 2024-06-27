from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
    

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": "1"}


def test_read_fake_item():
    item_id = 2
    response = client.get(f"/fake_items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"item_name": "Baz"}
    
    
def test_read_fake_item_2():
    item_id = 2
    response = client.get(f"/fake_items/?item_id={item_id}")
    assert response.status_code == 200
    assert response.json() == {"item_name": "Baz"}
    
    
def test_create_person():
    body = {"name": "Mike", "age": 30, "gender" : "male"}
    response = client.post("/person", json=body)
    assert response.status_code == 200
    assert response.json() == body