from flask import Flask 

app = Flask(__name__)

@app.route("/")
def home():
    return "Hos Geldiniz!"

@app.route("/about")
def about():
    return "Bu basit bir flask uygulamasidir."

if __name__ == "__main__":
    app.run(debug=True)