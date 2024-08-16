from recor_product_transformer.requests.woocommerce.woocommerce_base_request import WooCommerceBaseRequest
from typing import cast

REQUEST_PATH = "/wp-json/wc/v3/products"

class WooCommerceListAllProductsRequest(WooCommerceBaseRequest):
    def run(self) -> dict:
        response = self.session.get(self.base_url + REQUEST_PATH)
        if response.ok:
            return cast(dict, response.json())
        else:
            raise Exception(response.text)
