import dvc.api

with dvc.api.open(
        "get-started/data.xml",
        repo="https://github.com/iterative/dataset-registry"
) as fd:
    fd.read()  # this will loaded into workspace and see if exits in the machine
   # used for loading models and tracked metrcis and all.
