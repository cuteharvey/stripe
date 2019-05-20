import stripe

class charge(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def post_charge(self, amount, currency, source, receipt_email, description):
        # there are a lot more variables that can be passed but limiting it to these parameters for now.
        stripe.api_key = self.api_key

        try:
            response = stripe.Charge.create(
                amount=amount,
                currency=currency,
                source=source,
                receipt_email=receipt_email,
                description=description
            )
            print response
            return response
        except Exception as e:
            print(e)
            return e


