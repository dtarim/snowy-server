from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Başlangıçta boş bir hava durumu listesi
weather_data = []

# Ana Sayfa: Hava durumu tablosunu göster
@app.route("/")
def home():
    return render_template("home.html", weather_data=weather_data)

# Yeni şehir ekleme veya güncelleme
@app.route("/add", methods=["POST"])
def add_weather():
    new_city = request.json.get("city")  # Şehir adı
    new_weather = request.json.get("weather")  # Hava durumu bilgisi

    # Eksik veri kontrolü
    if not new_city or not new_weather:
        return jsonify({"error": "Şehir ve hava durumu bilgisi gerekli!"}), 400  

    # Mevcut şehri güncelle
    for item in weather_data:
        if item["city"].lower() == new_city.lower():
            item["weather"] = new_weather
            return jsonify({"message": f"{new_city} için hava durumu güncellendi!"}), 200

    # Yeni şehir ekleme
    weather_data.append({"city": new_city, "weather": new_weather})
    return jsonify({"message": "Veri başarıyla eklendi!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Docker içinde çalışacağı için 0.0.0.0'ı dinliyoruz
