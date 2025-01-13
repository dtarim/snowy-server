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
    response = client.post("/add", json={"city": "Eindhoven", "weather": "23 derece"})
    assert response.status_code == 200
    assert b"veri basariyla tabloya eklendi!" in response.data  #tablonun baslangicta bos oldugunu dogrula

    #tabloyu kontrol et
    response = client.get("/")
    assert response.status_code == 200
    assert b"Eindhoven" in response.data
    assert b"23 derece" in response.data