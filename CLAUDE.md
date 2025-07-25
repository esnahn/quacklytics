# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Quacklytics is a data analysis project that uses DuckDB for efficient processing of large datasets, particularly Korean building registry data (건축물대장). The project combines Python, Jupyter notebooks, and SQL to analyze building permits, construction data, and perform text classification using naive Bayes models.

## Development Environment Setup

```bash
# Create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux  
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Additional system dependencies (Windows with Scoop)
scoop install python iconv gawk
```

## Key Commands

### Data Processing
```bash
# Build administrative code mappings (법정동코드)
python scripts/build_bjdong.py

# Generate directory structure
python tree.py
```

### Jupyter Notebooks
```bash
# Start Jupyter environment
jupyter notebook notebooks/

# Key notebooks for data loading:
# - hub_data loading_건축물대장.ipynb
# - hub_data loading_인허가.ipynb
# - sample_duckdb.ipynb (DuckDB usage examples)
```

## Architecture Overview

### Data Structure
- **`data/raw/`** - Original source data files (Korean government datasets)
- **`data/processed/`** - Cleaned and processed CSV files
- **`data/*.db`** - DuckDB database files for efficient querying
- **`data/재조달원가/`** - Replacement cost data for buildings

### Analysis Workflow
1. **Data Loading**: Raw Korean text data (EUC-KR encoded) is loaded and converted to UTF-8
2. **DuckDB Processing**: Large datasets are processed using DuckDB for memory efficiency  
3. **Text Analysis**: Building usage descriptions are analyzed using naive Bayes classification
4. **Results Export**: Analysis results are saved to CSV files in `results/`

### Key Data Types
- **건축물대장** (Building Registry): Core building information including usage, structure, and permits
- **법정동코드** (Administrative Codes): Korean administrative district codes for geographic analysis
- **재조달원가** (Replacement Cost): Economic valuation data for buildings

### Notebooks Organization
- **hub_data loading_*.ipynb** - Data ingestion and initial processing
- **hub_건축물대장_*.ipynb** - Building registry analysis workflows
- **hub_인허가_*.ipynb** - Permit and licensing data analysis
- ***_naive bayes*.ipynb** - Text classification models for building usage prediction

## DuckDB Integration Patterns

```python
# Standard DuckDB workflow
import duckdb
con = duckdb.connect("data/건축물대장_2023_12.db")
result = con.sql("SELECT * FROM table_name WHERE condition").df()
```

DuckDB is used extensively for:
- Large CSV file processing without loading into memory
- SQL-based data transformations on pandas DataFrames
- Persistent storage of processed datasets

## Text Processing Notes

- Korean text data requires careful encoding handling (EUC-KR → UTF-8)
- Building usage descriptions contain mixed Korean/numeric text requiring specialized tokenization
- Naive Bayes models are trained on building usage text to predict usage categories

## Output Conventions

- Results are saved to `results/` directory with descriptive Korean filenames
- CSV files use UTF-8-BOM encoding for Korean text compatibility
- Analysis outputs include both summary tables and detailed predictions