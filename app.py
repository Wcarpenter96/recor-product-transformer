from transformers.iml.iml_product_transformer import RecorProductTransformer

def main(event: dict, *args: List[Any], **kwargs: Dict[Any, Any]):
    """
    :param event: event
    """
    transformer = RecorProductTransformer()

    transformer.transform(event)
