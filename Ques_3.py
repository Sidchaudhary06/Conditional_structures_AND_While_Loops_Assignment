gender = input("Enter biological gender (male/female): ").lower()
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

female_low = 117
female_high = 155
male_low = 134
male_high = 167

if gender == "female":
    if hemoglobin < female_low:
        print("Hemoglobin level is low for an adult female.")
    elif female_low <= hemoglobin <= female_high:
        print("Hemoglobin level is normal for an adult female.")
    else:
        print("Hemoglobin level is high for an adult female.")
elif gender == "male":
    if hemoglobin < male_low:
        print("Hemoglobin level is low for an adult male.")
    elif male_low <= hemoglobin <= male_high:
        print("Hemoglobin level is normal for an adult male.")
    else:
        print("Hemoglobin level is high for an adult male.")
else:
    print("Invalid gender entered. Please enter 'male' or 'female'.")
