# dvc_understanding
This is for understanding for DVC, A machine Learning tool which can track the data, Experiments and metrics.


**DVC**: Data version control, This is a tool for Machine Learning or Data scientis which can keep track of experiments, Metrics and Data using this tool. Basically Git is used for tracking the code and It has very limited size to keep track of file, and If we will large sized data sets to work on ML based Training then for git, it would be difficult so DVC supports this to keep the data file in some storage and linked with git for giving status of data version.
So, basically dvc create .dvc file which keep track of hash/MD5 value for latest data but It keeps tracks of all version of data in cache with MD5/hash key for each data version.

For working DVC, Install DVC 

    using PIP: pip install dvc
    Uisng conda: https://anaconda.org/conda-forge/dvc

Once installation is finished.
run following commands:

     DVC init: Which is used for initilising the dvc
     git init: git inialisation

after this, we can add the file in git for tracking code and **.dvc** file but NOT DATA FOLDER [This is only for DVC not for git]

Data storage could be anywhere: for storing data in google drive use:

    dvc remote add -d storage gdrive: hash_key_from_google_drive_folder; used for uploading data to storage.
    dvc push; This is used for pushing data into storegae
    dvc pull; for pulling the data from storage

using dvc accessing the model.

    dvc list; Which is used for tracking the dvc based file in github repo
    dvc list github.com/clone_project
    dvc get github.com/clone_project/data; it helps to get the file which you want to get into
    dvc get https://github.com/iterative/dataset-registry use-cases/cats-dogs/
    dvc import https://github.com/iterative/dataset-registry use-cases/cats-dogs/

to acess the dvc api
    follow python_api_dvc.api file
    using dvc.ap we can read the data and work on it for our purpose.

**Data pipelines**

  ***dvc stage add***: Used for creating stages. These represent processing steps (usually scripts/code tracked with Git) and combine to form the pipeline. This will generate a dvc.yaml file which keeps track of stages i.e what are the params and command is being used for running it.
  So, basically in the data pipelines, we can add the stages that "what should run first with thier depencies, data folder and information for running that particular pipleline."
  We can create data preparation, data featuraziation and training with all the depencies.

    The stages will look like this
      stages:
        prepare:
          cmd: python src\prepare.py .\data\data.xml
          deps:
          - .\data\data.xml
          - .\src\prepare.py
          params:
          - prepare.seed
          - prepare.split
          outs:
          - .\data\prepared
        featurize:
          cmd: python src/featurization.py data\prepared data\features
          deps:
          - data/prepared
          - src/featurization.py
          params:
          - featurize.max_features
          - featurize.ngrams
          outs:
          - data/features
        train:
          cmd: python src/train.py data/features model.pkl
          deps:
          - data/features
          - src/train.py
          params:
          - train.min_split
          - train.n_est
          - train.seed
          outs:
          - model.pkl
        evaluate:
          cmd: python src/evaluate.py model.pkl data/features
          deps:
          - data/features
          - model.pkl
          - src/evaluate.py
          outs:
          - eval/importance.png
          - eval/live/plots:
              cache: false
          - eval/prc:
              cache: false
          metrics:
          - eval/live/metrics.json:
              cache: false

   Then after this we can run
    DVC repro: which will reproduce this pipelines.
    DVC dag: shows the visualisation of pipelines
    dvc metrics show: It will show the metrcis which saved into eval/live folder.

    After changing the paramater, we can run again and see what are the changes happend.
    run dvc repro
    & see the changes.
    dvc params diff : which show the differt params is being used.
    dvc metrics diff : which shows the different metric changes


Important links:

Basic introduction: https://www.youtube.com/watch?v=mHQPzVse2oA&t=20s&ab_channel=KrishNaik

Official page: https://dvc.org/doc/start

DVC playlist: https://www.youtube.com/playlist?list=PL7WG7YrwYcnDb0qdPl9-KEStsL-3oaEjg



