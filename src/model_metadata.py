class ModelMetadata:
    name = None
    version = None

    def __str__(self):
        return f"Model name: {self.name} version: {self.version}"
