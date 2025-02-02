from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Baslangicta bu tabloyu bos birakiyoruz
weather_data = []

# Ana sayfa: tabloyu goster
@app.route("/")
def home():
    return render_template("home.html", weather_data=weather_data)

# POST ile tabloya veri ekleme veya güncelleme
@app.route("/add", methods=["POST"])
def add_weather():
    new_city = request.json.get("city")  # Şehir adı
    new_weather = request.json.get("weather")  # Hava durumu bilgisi

    # Veri dogrulama
    if not new_city or not new_weather:
        return jsonify({"error": "Şehir ve hava durumu bilgisi gerekli!"}), 400  # Girinti düzeltildi

    for item in weather_data:
        if item["city"].lower() == new_city.lower():
            item["weather"] = new_weather  # Güncelleme yapılıyor
            return jsonify({"message": f"{new_city} için hava durumu güncellendi!"}), 200

    # Yeni veriyi tabloya ekle
    weather_data.append({"city": new_city, "weather": new_weather})
    return jsonify({"message": "Veri başarıyla tabloya eklendi!"}), 200