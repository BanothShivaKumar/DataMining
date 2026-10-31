"""Generate synthetic demo data for the household electricity classification project.

This is demonstration data only, not the original project dataset.
"""
from pathlib import Path
import random
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
RANDOM_SEED = 42
N = 500

def classify_consumption(appliances, ac_hours, floor_area, efficient_pct, water_heater):
    score = (
        appliances * 1.4
        + ac_hours * 2.2
        + floor_area / 120
        + (1 - efficient_pct / 100) * 8
        + (5 if water_heater == "Yes" else 0)
    )
    if score < 28:
        return "Low"
    if score < 42:
        return "Medium"
    if score < 57:
        return "High"
    return "Very_High"

def main():
    rng = random.Random(RANDOM_SEED)
    rows = []
    for _ in range(N):
        appliances = rng.randint(2, 15)
        ac_hours = round(rng.uniform(0, 16), 1)
        floor_area = rng.randint(450, 3500)
        efficient_pct = rng.randint(0, 100)
        water_heater = rng.choice(["Yes", "No"])
        category = classify_consumption(
            appliances, ac_hours, floor_area, efficient_pct, water_heater
        )
        rows.append({
            "Num_Appliances": appliances,
            "AC_Hours_Day": ac_hours,
            "Floor_Area_sqft": floor_area,
            "Efficient_Appliance_Pct": efficient_pct,
            "Water_Heater": water_heater,
            "Consumption_Category": category,
        })

    csv_path = DATA_DIR / "household_electricity_demo.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    arff_path = DATA_DIR / "household_electricity_demo.arff"
    with arff_path.open("w", encoding="utf-8") as f:
        f.write("% SYNTHETIC DEMONSTRATION DATA — not original experimental data\n")
        f.write("@relation household_electricity_demo\n\n")
        f.write("@attribute Num_Appliances numeric\n")
        f.write("@attribute AC_Hours_Day numeric\n")
        f.write("@attribute Floor_Area_sqft numeric\n")
        f.write("@attribute Efficient_Appliance_Pct numeric\n")
        f.write("@attribute Water_Heater {Yes,No}\n")
        f.write("@attribute Consumption_Category {Low,Medium,High,Very_High}\n\n")
        f.write("@data\n")
        for r in rows:
            f.write(
                f'{r["Num_Appliances"]},{r["AC_Hours_Day"]},'
                f'{r["Floor_Area_sqft"]},{r["Efficient_Appliance_Pct"]},'
                f'{r["Water_Heater"]},{r["Consumption_Category"]}\n'
            )

    print(f"Wrote {len(rows)} synthetic rows:")
    print(f"  {csv_path}")
    print(f"  {arff_path}")

if __name__ == "__main__":
    main()
