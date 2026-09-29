# Data Reconciliation System

A Python-based data reconciliation project built using **Pandas** and **DataComPy**.

The project compares source and target datasets and identifies:

* Missing or new records
* Changed values
* Column differences
* Overall PASS / FAIL status

## Tech Stack

* Python
* Pandas
* DataComPy `1.0.4`
* PyYAML
* Pytest

## Project Structure

```text
data-reconciliation/
├── config/
├── data/
│   ├── source/
│   └── target/
├── src/
├── tests/
├── output/
├── main.py
├── requirements.txt
└── README.md
```

## Setup

Create a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Run

```powershell
python main.py
```

Comparison results are generated in the `output/` directory.

## Test

```powershell
pytest
```

## Goal

Build a reusable and configuration-driven data reconciliation framework using DataComPy.
