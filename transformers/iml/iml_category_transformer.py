from transformers.transformer import Transformer


class ImlCategoryTransformer(Transformer):
    def transform(self, raw_json: dict):
        """
        :param raw_json: raw_json
        """
        return raw_json
