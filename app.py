from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

#baslangicta bu tabloyu bos birakiyoruz
weather_data = []

#ana sayfa: tabloyu goster
@app.route("/")
def home():
    return render_template("home.html", weather_data=weather_data)

#POST ile tabloya veri ekleme
@app.route("/add", methods= ["POST"])
def add_weather():
    new_city = request.json.get("city") #sehir adi
    new_weather = request.json.get("weather") #hava durumu bilgisi

    #veri dogrulama
    if not new_city or not new_weather:
        return jsonify({"error": "sehir ve hava durumu bilgisi gerekli!"}), 400

    for item in weather_data:
        if item["city"].lower() == new_city.lower():
            return jsonify({"error" : f"{new_city} zaten tabloya eklenmis!"}), 400

    for item in weather_data:
        if item ["city"].lower() == new_city.lover():
            item["weather"] = new_weather
            return jsonify({"message": f"{new_city} icin hava durumu guncellenmistir!"}), 200
            
    #yeni veriyi tabloya ekle
    weather_data.append({"city": new_city, "weather": new_weather})
    return jsonify({"message": "veri basariyla tabloya eklendi!"}), 200

if __name__ == "__main__":
    app.run(debug=True)