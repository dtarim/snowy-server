import app

def test_home():
    # test client oluştur
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hos Geldiniz!" in response.data

def test_about():
    # about endpointini test et
    client = app.app.test_client()
    response = client.get("/about")
    assert response.status_code == 200
    assert b"Bu basit bir flask uygulamasidir." in response.data
