try:
    import pickle

    model = pickle.load(open("../model.pkl", "rb"))

    print("=== Insulin Resistance Risk Predictor ===\n")

    age = int(input("Age: "))
    waist = int(input("Waist (cm): "))
    height = int(input("Height (cm): "))

    activity = input("Activity (Low/Medium/High): ").capitalize()
    sleep = int(input("Sleep hours: "))
    sugar = input("Sugar intake (Low/Medium/High): ").capitalize()
    family = int(input("Family History (0/1): "))
    stress = input("Stress (Low/Medium/High): ").capitalize()
    water = float(input("Water intake (litres): "))

    activity_map = {"Low": 0, "Medium": 1, "High": 2}
    sugar_map = {"Low": 0, "Medium": 1, "High": 2}
    stress_map = {"Low": 0, "Medium": 1, "High": 2}

    input_data = [[
        age, waist, height,
        activity_map[activity],
        sleep,
        sugar_map[sugar],
        family,
        stress_map[stress],
        water
    ]]

    prediction = model.predict(input_data)

    risk_map = {0: "Low", 1: "Moderate", 2: "High"}

    print("\nPredicted Risk:", risk_map[prediction[0]])

except Exception as e:
    print("\nERROR:", e)

input("\nPress Enter to exit...")