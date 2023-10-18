import os

from xpate_sdk import Xpate


# Set these to your actual endpoint and API key
endpoint = os.getenv('XPATE_ENDPOINT')
api_key = os.getenv('XPATE_API_KEY')

# Get our client
client = Xpate.create_client(endpoint, api_key)

# Create our order without specifying a payment method
order = client.create_order({
    'amount': 250,  # Amount in cents
    'currency': 'EUR',
})

# Show the order URL where the user can select a payment method and initiate the transaction
print('Payment URL:', order['order_url'])
