from django.shortcuts import render
import requests

url = "https://v6.exchangerate-api.com/v6/2b5a68ad0e2638ee61dd3060/pair/USD/BRL"

#polish zlot converter
def index(request):
    amount_converted = None
    if request.method == "POST":
        amount = float(request.POST['amount'])
        response = requests.get(url)
        zloty_to_dollar_rate = response.json()['conversion_rate']
        amount_converted = round(amount * zloty_to_dollar_rate, 2)
    return render(request, 'converter/index.html', {'conversion_result': amount_converted, 'currency': 'PLN'})

def brazilian_real(request):
    amount_converted = None
    if request.method == "POST":
        amount = float(request.POST['amount'])
        response = requests.get(url)
        zloty_to_dollar_rate = response.json()['conversion_rate']
        amount_converted = round(amount * zloty_to_dollar_rate, 2)
    return render(request, 'converter/index.html', {'conversion_result': amount_converted, 'currency': 'BRL'})
