from flask import Flask, render_template, request
import random

app = Flask(__name__)

fact_list = [
    "🐱 Kedilerin beyninde 300 milyondan fazla nöron bulunur.",
    "🌙 Ay, Dünya’dan her yıl yaklaşık 3.0 cm uzaklaşır.",
    "✨ Yıldızlar gündüz de gökyüzünde ama Güneş ışığı onları gizler.",
    "☀️ Güneşin sıcaklığı her yıl biraz artıyor.",
    "👽 Kediler uzaylıdır! ❤️😁"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/random-fact")
def random_fact():
    return f"<h2 style='text-align:center;'>{random.choice(fact_list)}</h2>"

@app.route('/hello', methods = ["GET", "POST"])
def hello():
    if request.method == "POST":
        name = request.form.get("name")
        return f"<h1 style='text-align:center;'>Merhaba {name}! 👋</h1>"
    return '''
        <form method="POST" style="text-align:center; margin-top:50px;">
            <p>İsmini yaz ve sana merhaba diyeyim! 😊</p>
            <input type="text" name="name" placeholder="İsmin ne?" style="padding:8px; border-radius:5px; border:1px solid #ccc;">
            <button type="submit" style="padding:8px 15px; background:#28a745; color:white; border:none; border-radius:5px; cursor:pointer;">
                Gönder
            </button>
        </form>
    '''

app.run(debug=True)