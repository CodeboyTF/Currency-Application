import requests
from django.shortcuts import render
from datetime import datetime


def index(request):
    result = None
    currencies = []

    # Getting list of currencies
    symbols_url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json'
    symbols_response = requests.get(symbols_url).json()

    if symbols_response:
        currencies = list(symbols_response.keys())
    else:
        currencies = ['usd', 'zar', 'eur']

    if request.GET.get('amount') and request.GET.get('from_currency') and request.GET.get('to_currency'):
        amount = request.GET.get('amount')
        from_currency = request.GET.get('from_currency').lower()
        to_currency = request.GET.get('to_currency').lower()

        try:
            float_amount = float(amount)

            # Getting current date in YYYY-MM-DD format
            today = datetime.now().strftime('%Y-%m-%d')
            url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{today}/v1/currencies/{from_currency}.json"
            response = requests.get(url).json()

            if from_currency in response and to_currency in response[from_currency]:
                rate = response[from_currency][to_currency]
                converted_amount = float_amount * rate

                result = {
                    'original': amount,
                    'converted': round(converted_amount, 2),
                    'from_currency': from_currency.upper(),
                    'to_currency': to_currency.upper()
                }
            else:
                result = {
                    'error': "Currency conversion not available"
                }

        except ValueError:
            result = {'error': "Please enter a valid number"}
        except Exception as e:
            result = {'error': f"An error occurred: {str(e)}"}

    return render(request, 'Calculator/index.html', {
        'result': result,
        'currencies': [currency.upper() for currency in currencies]
    })