import unittest
import stripe
from api_stripe.api_methods.api_credentials import api_credentials
from api_stripe.api_methods.balances_methods import balances

class test_api_balance(unittest.TestCase):

    def test_balance(self):
        """Tests the balance endpoint
        https://stripe.com/docs/api/balance
        """

        #get api key from the api credentials object/method
        api_key = api_credentials().get_api_key()
        balance = balances(api_key)
        # send a get method to stripe balance endpoint
        response = balance.get_balance()
        # get list of supported balances from the balance object/method
        supported_currencies = balance.get_supported_currencies()
        for balance in response['available']:
            current_currency = balance['currency']
            # verify that the currency returned in the response is a supported currency
            assert current_currency in supported_currencies, "%s currency not found in %s" % (current_currency, supported_currencies)
            # print balance and currency to console
            print "User has a balance of %s %s" % (balance['amount'], balance['currency'])
            # verify that for every currency that bank_account, bitcoin_receiver and card nodes exist
            assert type(balance['source_types']['card']) is int, "bank account node not found for %s currency" % current_currency
            assert type(balance['source_types']['card']) is int, "bitcoin receiver not found for %s currency" % current_currency
            assert type(balance['source_types']['card']) is int, "card not found for %s currency" % current_currency


if __name__ == "__main__":
    pass
