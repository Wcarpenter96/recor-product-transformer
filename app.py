from typing import Any, List, Dict

from requests.woocommerce.woocommerce_list_all_products_request import WooCommerceListAllProductsRequest
from transformers.iml.iml_product_transformer import ImlProductTransformer


def main(event: dict, *args: List[Any], **kwargs: Dict[Any, Any]):
    """
    :param event: event
    """
    products = WooCommerceListAllProductsRequest()
    transformer = ImlProductTransformer()

    transformer.transform(products)

    return products

