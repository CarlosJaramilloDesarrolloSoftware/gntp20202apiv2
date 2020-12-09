from flask import Flask, render_template, url_for, redirect
import requests
from requests.api import request

app = Flask(__name__)
app.secret_key = "sdfg976dsfg"

@app.route('/')
def index():
    url = 'https://api.ratesapi.io/api/latest'
    paramss = {'base':'USD'}

    res = requests.request("GET", url, params = paramss)
    if res.status_code == 200:
        body = res.json()
        base = body["base"]
        fecha = body["date"]
        records = body["rates"]
        return render_template('index.html', base = base, fecha = fecha, records = records)
    else:
        return render_template('error.html')

@app.route('/detail/<base>')
def detail(base):
    url = 'https://api.ratesapi.io/api/latest'
    paramss = {'base':base}

    res = requests.request("GET", url, params = paramss)
    if res.status_code == 200:
        body = res.json()
        base = body["base"]
        fecha = body["date"]
        records = body["rates"]
        return render_template('index.html', base = base, fecha = fecha, records = records)
    else:
        return render_template('error.html')

@app.route('/converter')
def converter(base = "USD"):
    url = 'https://api.ratesapi.io/api/latest'
    paramss = {'base':base}

    res = requests.request("GET", url, params = paramss)
    if res.status_code == 200:
        body = res.json()
        records = body["rates"]
        return render_template('converter.html', records = records)
    else:
        return render_template('error.html')

@app.route('/result', methods=['POST'])
def result():
    base = request.form['moneda_actual']
    symbol = request.form['moneda_destino'] 
    cantidad = request.form['cantidad']

    url = 'https://api.ratesapi.io/api/latest'

    paramss = {'base':base, 'symbols': symbol}

    res = requests.request("GET", url, params = paramss)
    if res.status_code == 200:
        body = res.json()
        result = body["rates"][symbol] 
        return render_template('result.html', result = result)
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)