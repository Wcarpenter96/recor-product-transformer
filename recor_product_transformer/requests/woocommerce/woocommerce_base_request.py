import os
import requests


class WooCommerceBaseRequest:
    def __init__(self):
        self.base_url = os.getenv('WOOCOMMERCE_BASE_URL')
        self.session = requests.Session()
        self.session.auth = (os.getenv('WOOCOMMERCE_CONSUMER_KEY'), os.getenv('WOOCOMMERCE_CONSUMER_SECRET'))
