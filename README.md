INSULIN RESISTANCE PREDICTOR

&#x20;Insulin resistance is one of the leading chronic diseases in India. It lowers stamina, gives a headache, makes the person take more supplements, and many more negative effects which go unnoticed in the early stages



Overview:

This project predicts the risk level of insulin resistance based on lifestyle and physical factors such as waist size, sleep, activity level and diet

It is a preventative tool and not a medical diagnostic system





FEATURES:

1. Takes user input ( age, activity and sleep, etc)
2. Predicts risk level: low/medium/high
3. Uses Machine Learning (decision tree)









Project structure

1. data- contains a dataset from trusted sources
2. src- contains the Python code
3. readme.md - project instructions





**HOW TO RUN THE PROGRAM**

**1)Install the required libraries ( pip install pandas , scikit-learn)**

**2) Run the prediction script :**

**python src/predict.py**





**EXAMPLE INPUT**

**Age- 22**

**waist- 85**

**activity - low**

**sleep - 5**





EXAMPLE OUTPUT

Predicted risk - HIGH.



Key point - Using BMI is slightly misleading, esp in India, where diabetes types 1 and 2 are seen almost everywhere. BMI calculates the weight and height ratio but does not differentiate between muscle mass and fat mass. Women (adults) have more weight around the chest and hips naturally due to estrogen.





(NOTE- This model is based on a small synthetic dataset and is intended for educational purposes only )

