import unittest
from api_stripe.api_methods.api_credentials import api_credentials
from api_stripe.api_methods.charge_methods import charge

class test_api_charge_create(unittest.TestCase):

    def test_charge_create_happy_path(self):
        """Tests the create charges endpoint
        https://stripe.com/docs/api/charges/create
        """
        # Test Case: Happy Path
        amount = 1000
        currency = "usd"
        source = "tok_visa"
        receipt_email = "testonly@testonly.com"
        description = "for testing purposes only"

        # get api key from the api credentials object/method
        api_key = api_credentials().get_api_key()
        charges = charge(api_key)
        # send a post method to stripe create charges endpoint
        response = charges.post_charge(amount, currency,source,receipt_email,description)

        # verify the amount in the response
        assert response['amount'] == amount, "Amount in response: %s. Expecting %s" % (response['amount'], amount)
        # verify currency in the response
        assert response['currency'] == currency, "Currency in response: %s. Expecting %s" % (response['currency'], currency)
        # receipt email
        assert response['receipt_email'] == receipt_email, "Email in response: %s. Expecting %s" % (response['receipt_email'], receipt_email)
        # verify description
        assert response['description'] == description, "Description in response: %s. Expecting %s" % (response['description'], description)

    def test_charge_create_invalid_api_key(self):
        # Test Case: invalid api key
        amount = 1000
        currency = "usd"
        source = "tok_visa"
        receipt_email = "testonly@testonly.com"
        description = "for testing purposes only"

        api_key = "invalid_key"
        charges = charge(api_key)
        response = charges.post_charge(amount, currency,source,receipt_email,description)
        # verify error message received
        # Invalid API Key provided: invalid_key
        assert "Invalid API Key provided: %s" % api_key in response

    def test_charge_create_missing_field_amount(self):
        # Test Case: do not pass amount in payload
        api_key = api_credentials().get_api_key()
        charges = charge(api_key)
        response = charges.post_charge_negative_missing_amount()
        # verify error message received
        # Request req_rBFrzOF0P7lzqZ: Missing required param: amount.
        assert "Missing required param: amount." in response

    def test_charge_create_negative_amount(self):
        # Test Case: negative amount
        amount = -10
        currency = "usd"
        source = "tok_visa"
        receipt_email = "testonly@testonly.com"
        description = "for testing purposes only"

        api_key = api_credentials().get_api_key()
        charges = charge(api_key)
        response = charges.post_charge(amount, currency,source,receipt_email,description)
        # verify error message received
        # expected error returned: Request req_Y9aAYCbqXt5c3l: Invalid positive integer
        assert "Invalid positive integer" in response

    def test_charge_create_amount_with_decimal(self):
        # Test Case: amount with decimals
        amount = 100.25
        currency = "usd"
        source = "tok_visa"
        receipt_email = "testonly@testonly.com"
        description = "for testing purposes only"

        api_key = api_credentials().get_api_key()
        charges = charge(api_key)
        response = charges.post_charge(amount, currency,source,receipt_email,description)
        # verify error message received
        # expected error returned: Request req_je8PC0Kyqfr3Rf: Invalid integer: 100.25
        assert "Invalid integer: %s" % amount in response

    def test_charge_create_invalid_email(self):
        # Test Case: invalid email address
        amount = 1000
        currency = "usd"
        source = "tok_visa"
        receipt_email = "testonlytestonly.com"
        description = "for testing purposes only"

        api_key = api_credentials().get_api_key()
        charges = charge(api_key)
        response = charges.post_charge(amount, currency,source,receipt_email,description)
        # verify error message received
        # expected error returned: Request req_Ctol7qJ2UpFhue: Invalid email address: testonlytestonly.com
        assert "Invalid email address: %s" % receipt_email in response

    """Other test cases to perform:
    - null API key
    - other missing required fields eg. do not pass currency param in payload, ...
    - extra param that is not supported
    - too big amount eg. 99999999999999
    - upper cases on currency and source
    - invalid currency
    - special characters on each of the fields
    - null values for each of the fields
    - empty string for currency, source, receipt and/or email
    """


if __name__ == "__main__":
    pass
