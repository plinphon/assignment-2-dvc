# Lesson 1 tutorial: Get started 
**Machine Learning REPA community tutorial**: Get started with Data Version Control (DVC)

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
