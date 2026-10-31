# Data Mining Project

## Household Electricity Consumption Category Prediction Using ZeroR, OneR and J48 Decision Tree in WEKA

**Course:** Data Mining (A8526)  
**Institution:** Vardhaman College of Engineering, Hyderabad  
**Team Number:** 03  
**Project Type:** Classification using Data Mining Techniques

## Project Overview

This project focuses on predicting household electricity consumption categories using data mining classification algorithms. Three classifiers are considered: ZeroR, OneR, and J48 Decision Tree.

The goal is to compare their classification performance and understand how household attributes relate to electricity consumption categories.

## Algorithms Used

- **ZeroR:** Baseline classifier that predicts the majority class.
- **OneR:** Classification algorithm that creates rules using a single attribute.
- **J48 Decision Tree:** Decision-tree classifier used to model relationships between household features and consumption categories.

## Dataset Attributes

The project uses the following attributes:

- `Num_Appliances`
- `AC_Hours_Day`
- `Floor_Area_sqft`
- `Efficient_Appliance_Pct`
- `Water_Heater`
- `Consumption_Category` — target class

The consumption categories are `Low`, `Medium`, `High`, and `Very_High`.

## Project Structure

```text
DataMining/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── household_electricity_demo.arff
├── docs/
│   └── weka_commands.md
└── src/
    └── generate_demo_dataset.py
```

## Tools and Technologies

- WEKA
- Python
- ARFF dataset format
- Git and GitHub

## Running the Demo Dataset Generator

Make sure Python is installed. From the project directory, run:

```bash
python src/generate_demo_dataset.py
```

This generates a synthetic demonstration dataset in CSV and ARFF formats.

## Running the Classifiers in WEKA

Open the ARFF dataset in WEKA Explorer, select the **Classify** tab, choose a classifier, and select 10-fold cross-validation to evaluate it.

Example command-line instructions are available in `docs/weka_commands.md`.

## Results

The project report records the following 10-fold cross-validation accuracy values:

| Classifier | Reported Accuracy |
|---|---:|
| ZeroR | 33.00% |
| OneR | 42.60% |
| J48 Decision Tree | 80.00% |

These values are reproduced from the project report and have not been independently verified against the original dataset.

## Important Dataset Note

The included generator creates **synthetic demonstration data**. It is not the original experimental dataset. Use the actual project dataset and rerun the classifiers in WEKA before treating the reported results as independently verified.

## Conclusion

The project compares a baseline classifier, a single-attribute rule classifier, and a decision-tree classifier for household electricity consumption categorization. The reported results show J48 performing best among the three models in the project report.
