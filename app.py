from flask import Flask, render_template, request, jsonfy

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
        return jsonfy({"error": "sehir ve hava durumu bilgisi gerekli!"}), 400

    #yeni veriyi tabloya ekle
    weather_data.append({"city": new_city, "weather": new_weather})
    return jsonfy({"message": "veri basariyla tabloya eklendi!"}), 200

if __name__ == "__main__":
    app.run(debug=True)