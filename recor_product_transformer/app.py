from typing import Any, List, Dict
import logging

from recor_product_transformer.requests.woocommerce.woocommerce_list_all_products_request import WooCommerceListAllProductsRequest
from recor_product_transformer.transformers.iml.iml_product_transformer import ImlProductTransformer

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def main(event: dict, *args: List[Any], **kwargs: Dict[Any, Any]):
    """
    :param event: event
    """
    products = WooCommerceListAllProductsRequest().run()
    transformer = ImlProductTransformer()

    transformer.transform(products)

    return products

