from flask import Flask, render_template, request, flash, redirect
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError


app = Flask(__name__)

rates = CurrencyRates()
codes = CurrencyCodes()

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/', methods = ["POST"])
def get_currency():
    converting_from = request.form['convert_from']
    converting_to = request.form['convert_to']
    value= float(request.form['amount'])
    symbol = codes.get_symbol(converting_to)
    final = round(rates.convert(converting_from, converting_to, value),2)
    return render_template('rate.html', final_rate = final, symbol=symbol)













