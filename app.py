from flask import Flask, render_template, request, flash, redirect
from forex_python.converter import CurrencyRates, CurrencyCodes


app = Flask(__name__)

rates = CurrencyRates()
codes = CurrencyCodes()

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/conversion', methods = ["POST"])
def get_currency():
   converting_from = request.form['convert_from']
   converting_to = request.form['convert_to']
try:
   value = float(request.form['amount'])
except:
    print("Not a valid amount")
try:
    symbols = codes.get_symbol(converting_to)
    final = rates.convert(converting_from, converting_to, value)
return render_template('rate.html', final_rate = final, symbol = symbols)
except UnavailableRateError:
    flash("Please enter a valid currency")
return redirect('/')
except (ValueError, TypeError):
    flash("Oops something went wrong")
return redirect ('/')






