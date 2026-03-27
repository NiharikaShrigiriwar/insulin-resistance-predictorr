import pandas as pd

data = pd.read_csv("../data/dataset.csv")

print("Dataset loaded successfully!\n")
print(data.head())

print("\nProgram finished.")
input("Press Enter to exit...")