# DataMining

## Household Electricity Consumption Category Prediction Using ZeroR, OneR and J48 Decision Tree in WEKA

Course project for Data Mining (A8526).

### Project overview
This project compares ZeroR, OneR, and J48 decision-tree classification for household electricity-consumption categories.

### Files
- `src/generate_demo_dataset.py` — generates a clearly labelled synthetic demonstration dataset.
- `data/household_electricity_demo.arff` — sample ARFF schema and demonstration records.
- `docs/weka_commands.md` — example WEKA command-line instructions.
- `requirements.txt` — Python dependencies for dataset generation.

### Important note
The original dataset and original WEKA output files were not available when this repository package was prepared. The included data is synthetic demo data and must not be presented as the original experimental dataset. Re-run the WEKA models on your actual dataset before reporting verified metrics.

### Run the demo data generator
```bash
python src/generate_demo_dataset.py
```

The script writes `data/household_electricity_demo.csv` and `data/household_electricity_demo.arff`.
