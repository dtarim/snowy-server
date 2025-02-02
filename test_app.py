import app

def test_home():
    # Test client oluştur
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "Hos Geldiniz!" in response.get_data(as_text=True)  # UTF-8 uyumlu hale getirildi

def test_add_weather():
    client = app.app.test_client()

    # Tabloya yeni veri ekleme
    response = client.post("/add", json={"city": "Eindhoven", "weather": "23"})
    assert response.status_code == 200
    response_data = response.get_json()  # JSON yanıtını parse et
    assert response_data["message"] == "Veri başarıyla tabloya eklendi!"  # Güncellendi

    # Aynı şehri tekrar eklediğimizde güncellenmeli ve 200 dönmeli
    response = client.post("/add", json={"city": "Eindhoven", "weather": "25"})
    assert response.status_code == 200  # Artık 400 beklemiyoruz, çünkü güncelleme oluyor!
    response_data = response.get_json()  # JSON yanıtını parse et
    assert response_data["message"] == "Eindhoven için hava durumu güncellendi!"  # Güncellendi