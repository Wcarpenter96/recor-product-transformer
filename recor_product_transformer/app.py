from typing import Any, List, Dict

from recor_product_transformer.requests.woocommerce import WooCommerceListAllProductsRequest
from recor_product_transformer.transformers.iml.iml_product_transformer import ImlProductTransformer


def main(event: dict, *args: List[Any], **kwargs: Dict[Any, Any]):
    """
    :param event: event
    """
    products = WooCommerceListAllProductsRequest()
    transformer = ImlProductTransformer()

    transformer.transform(products)

    return products

