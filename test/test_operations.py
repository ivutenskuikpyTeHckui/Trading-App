from httpx import AsyncClient
from .conftest import client

async def get_specific_operations(ac: AsyncClient):
    response = await ac.get("/operations", params={
        "operation_type": "string",
    })

    assert response.status_code == 200

def test_add_specific_operations():
    response =  client.post("/operations", json={
        "id": 1,
        "quantity": "25.5",
        "figi": "figi_CODE",
        "instrument_type": "bond",
        "date": "2023-02-01T00:00:00",
        "type": "Выплата купонов",
    })

    assert response.status_code == 200
