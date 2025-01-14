import app

def test_home():
    # test client oluştur
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hos Geldiniz!" in response.data

def test_add_weather():
    client = app.app.test_client()

    #tabloya veri ekle
    response = client.post("/add", json={"city": "Eindhoven", "weather": "23"})
    #tablonun baslangicta bos oldugunu dogrula
    assert response.status_code == 200
    assert b"veri basariyla tabloya eklendi!" in response.data

    response = client.post("/add", json={"city": "Eindhoven", "weather": "25"})
    #tabloya zaten eklenmis oldugunu dogrula
    assert response.status_code == 400
    assert b"Eindhoven zaten tabloya eklenmis!" in response.data