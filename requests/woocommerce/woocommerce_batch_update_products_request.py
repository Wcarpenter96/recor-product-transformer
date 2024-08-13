from woocommerce import API
import os

wcapi = API(
    url=os.getenv('WOOCOMMERCE_BASE_URL'),
    consumer_key=os.getenv('WOOCOMMERCE_CONSUMER_KEY'),
    consumer_secret=os.getenv('WOOCOMMERCE_CONSUMER_SECRET'),
    version="wc/v3"
)