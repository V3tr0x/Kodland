from flask import Flask
import random
app = Flask(__name__)

facts_list = ["Elon Musk twierdzi, że sieci społecznościowe zostały zaprojektowane tak, aby trzymać nas na platformie, abyśmy spędzali jak najwięcej czasu na przeglądaniu treści.",
"Według badania przeprowadzonego w 2018 r. ponad 50% osób w wieku od 18 do 34 lat uważa, że jest zależnych od swoich smartfonów.",
"Sieci społecznościowe mają swoje zalety i wady, a korzystając z tych platform, powinniśmy być ich świadomi.",
"Badanie uzależnień technologicznych jest jednym z najważniejszych obszarów współczesnych badań naukowych."]
flip_coin=['Orzeł',
           'Reszka']
@app.route("/")
def hello():
    return '<h1>Cześć zobacz kilka losowych faktów</h1>' '<a href="/random_fact">Zobacz losowy fakt!</a>'  '<br><a href="/coin_flip">Zalosuj monetą!</a>'
@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/coin_flip")
def FUNCTION_NAME():
    return f'<p>{random.choice(flip_coin)}</p>'

app.run(debug=True)