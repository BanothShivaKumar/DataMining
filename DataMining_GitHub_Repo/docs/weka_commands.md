# Example WEKA commands

Run these commands from a terminal where WEKA is installed. Update the path to your dataset as needed.

```bash
java -cp weka.jar weka.classifiers.rules.ZeroR -t data/household_electricity_demo.arff -x 10
java -cp weka.jar weka.classifiers.rules.OneR -t data/household_electricity_demo.arff -x 10
java -cp weka.jar weka.classifiers.trees.J48 -t data/household_electricity_demo.arff -x 10
```

These are example commands for the included synthetic demo dataset. Use the original dataset for your actual project results.
