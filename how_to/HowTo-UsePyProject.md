# How to use `pyproject.toml` in the SdPCR Project

This guide explains how to manage dependencies, build the project, and keep 
the environment isolated using `pyproject.toml`.

---

## 1. Setting Up Your Environment
### Option 1: Use `conda` (What we will use)
```bash
conda create -n sdpcr-env python=3.11
conda activate sdpcr-env
```

### Option 2: Use `venv` (Python built-in)

```bash
python3 -m venv .venv
source .venv/bin/activate # On macOS/Linux
# .venv\Scripts\activate # On Windows
``` 

## 2. Installing the Project and Dependencies
`pip install .`

## 3. Running the Project
You can now import and use sdpcr as a module (e.g. shown below):
`from sdpcr.core.ddpcr import simulate_ddpcr`
Or run any CLI scripts inside the `scripts/` directory:
`python scripts/run_simulation.py`

## 4. Building the Project
`python -m build`
This will create a `dist/` folder with `.whl` and `.tar.gz` files.
