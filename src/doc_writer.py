import os
from markdownmaker.markdownmaker import *


class DocWriter:
    doc_header = "Impact Resilience Models"

    def __init__(self, model_metadatas, doc_dir, doc_name):
        self.model_metadatas = model_metadatas
        self.doc_dir = doc_dir
        self.doc_name = doc_name
        self.doc = None

    def build_doc(self):
        document = Document()
        document.add(Header(DocWriter.doc_header))
        model_strings = []
        for model_data in self.model_metadatas:
            model_string = f'Model Name: {model_data.name} Version: {model_data.version}'
            model_strings.append(model_string)
        document.add(UnorderedList(model_strings))
        self.doc = document.write()
        print(self.doc)
        return self.doc

    def write_doc(self):
        filepath = os.path.join(self.doc_dir, self.doc_name)
        if not os.path.exists(self.doc_dir):
            os.makedirs(self.doc_dir)
        f = open(filepath, "w")
        f.write(self.doc)
        f.close()
