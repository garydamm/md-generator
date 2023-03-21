import re
from src.model_metadata import ModelMetadata

pattern = r'^impact_resilience_model: name=(.*), version=(.*)$'


def extract_model_metadata(comment):
    if comment:
        model_metadata = ModelMetadata()
        match = re.search(pattern, comment)
        if match:
            model_metadata.name = match.group(1)
            model_metadata.version = match.group(2)
            return model_metadata
        else:
            return None
    else:
        return None
