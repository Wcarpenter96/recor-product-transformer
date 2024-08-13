import json
import logging
from recor_product_transformer.app import main

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    logger.info(f"CloudWatch logs group: {context.log_group_name}")

    data = main(event)
    return json.dumps(data)

