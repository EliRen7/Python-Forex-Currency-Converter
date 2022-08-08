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

# @app.route('/', methods=['POST'])
# def process():
#     conv_from = request.form['convert_from']
#     conv_to = request.form['convert_to']
#     if request.form['amount'] == "":
#         print("Enter a valid amount")
#         return False
#     else:
#         amount = float(request.form['amount'])
    
#     try:
#         results = round(rates.convert(conv_from, conv_to, amount), 2)
#         symbol = codes.get_symbol(conv_to)
#         return render_template("rate.html", convert_from=conv_from, convert_to=conv_to, amount=amount, final_rate=results, symbol = symbol)
#     except RatesNotAvailableError:
#         flash("Please enter a valid currency")
#         return redirect('/')
#     except (ValueError, TypeError):
#         flash("Oops something went wrong")
#         return redirect('/')
   








