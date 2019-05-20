import stripe

class balances(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_supported_currencies(self):
        supported_currencies = ['cad', 'gbp', 'nzd', 'aud', 'jpy', 'brl', 'usd', 'sek', 'eur']

        return supported_currencies

    def get_balance(self):
        stripe.api_key = self.api_key
        try:
            response = stripe.Balance.retrieve()
            print response
            return response
        except Exception as e:
            print(e)
            return e

