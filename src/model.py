import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
data = pd.read_csv("../data/dataset.csv")

# Convert text to numbers
data["Activity"] = data["Activity"].map({"Low": 0, "Medium": 1, "High": 2})
data["Sugar"] = data["Sugar"].map({"Low": 0, "Medium": 1, "High": 2})
data["Stress"] = data["Stress"].map({"Low": 0, "Medium": 1, "High": 2})
data["Risk"] = data["Risk"].map({"Low": 0, "Moderate": 1, "High": 2})

# Split features and target
X = data.drop("Risk", axis=1)
y = data["Risk"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("../model.pkl", "wb"))

print("Model trained and saved!")
input("Press Enter to exit...")