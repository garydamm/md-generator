import sys
import pathlib
from comment_parser import comment_parser
from src.regex_comment_parser import extract_model_metadata
from src.doc_writer import DocWriter

src_path = "sample_files"
doc_dir = "model_metadata_doc"
doc_name = "impact_resilience_model_metadata.md"
python_mime_type = "text/x-python"

if len(sys.argv) == 2:
    src_path = sys.argv[1]
print(f'Using {src_path} as the python source path')

python_files = list(pathlib.Path(src_path).rglob("*.py"))
print("Found these .py files:")
print(python_files)

model_metadatas = []

for file in python_files:
    comments = comment_parser.extract_comments(file, mime=python_mime_type)
    for comment in comments:
        model_metadata = extract_model_metadata(comment.text().strip())
        if model_metadata:
            model_metadatas.append(model_metadata)
print("Built these metadata objects:")
print(model_metadatas)

print("Building output file")
doc_writer = DocWriter(model_metadatas, doc_dir, doc_name)
doc_writer.build_doc()

print(f"Writing File to {doc_dir}/{doc_name}")
doc_writer.write_doc()
