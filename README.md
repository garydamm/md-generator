Impact Resilience Model Documentation Generator
===========================

Project to auto generate a markdown document containing the metadata (name and version) of a model given a specific comment format in Python source code.

For example:
```python
# impact_resilience_model: name=model-1, version=1.0.0
```

# How to Run
```shell
pip install -r requirements.txt
python main.py sample_files
```
Where ```sample_files``` is the directory that contains the python source files.

This will generate a markdown file in a directory named ```model_metadata_doc```