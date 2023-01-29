# PyCashflow

Financial modelling for pandas users.

## Why PyCashflow?

Financial modelling with Excel can be a nightmare. These models are hard to
maintain, hard to extend, and hard to encode with any sophisticated logic.
PyCashflow provides the framework to construct sophisitcated financial models
using python-native constructs.

## Quickstart

```python
from pycashflow import FinancialModel, LineItem

model = FinancialModel("Simple Cashflow Model")

model["Revenue Stream #1"] = LineItem(lambda t: 1000)
model["Revenue Stream #2"] = LineItem(lambda t: 100 + 10*t)
model["Expense #1"] = LineItem(lambda t: 500)
model["Expense #2"] = LineItem(lambda t: 50 + 5*t)

model["Profit"] = (
    model["Revenue Stream #1"]
    + model["Revenue Stream #2"]
    - model["Expense #1"]
    - model["Expense #2"]
)

df = model.run(steps=24)
df.tail()
```

## Local Development

We rely on [`just`](https://github.com/casey/just) to act as our command runner.
It is not possible to install this via PyPI and instead you must rely on the
installation instructions on the Github page.

The most common installation method is to use conda. To create a new virtual
environment, install `just` and the package requirements, you can run the
following commands:

```bash
conda create -n pycashflow python just
# wait for this to complete...

conda activate pycashflow
pip install -e .[dev]
```
