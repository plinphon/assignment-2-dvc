# Lesson 1 tutorial: Get started 
**ML REPA School course**: Machine Learning experiments reproducibility and engineering with DVC

## 1. Clone this repository

```bash
git clone THIS_REPO
cd dvc-1-get-started
```

## 2. Create and activate virtual environment

Create virtual environment named `dvc` (you may use other name)
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install python libraries

```bash
pip install -r requirements.txt
```

## 4. Add Virtual Environment to Jupyter Notebook

```bash
python -m ipykernel install --user --name=dvc-101
```

## 5. Configure ToC for jupyter notebook (optional)

```bash
jupyter contrib nbextension install --user
jupyter nbextension enable toc2/main
```

## 6. Run and follow Jupyter Notebook `dvc-1-get-started.ipynb` for instructions:

```bash
jupyter notebook
```


## DVC pipeline 
```yaml 

stages:
  
  evaluate: 
    cmd: python src/featurize.py
    deps:
    - data/iris.csv
    - src/featurize.py
    outs:
    - data/features_iris.csv
  
  split_dataset: 
    cmd: python src/split_dataset.py
    deps:
    - data/features_iris.csv
    outs:
    - data/train.csv
    - data/test.csv
    
  train: 
    cmd: python src/train.py
    deps:
    - data/train.csv
    - data/test.csv
    outs:
    - data/model.joblib

  evaluate: 
    cmd: python src/evaluate.py
    deps:
    - data/model.joblib
    outs:
    - data/eval.txt

```  
