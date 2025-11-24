# BMI Calculator in python

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

print(" BMI Calculator ")

try:
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))

    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    print(f"\nYour BMI: {bmi}")
    print(f"Category: {category}")

except ValueError:
    print("Invalid input! Please enter numeric values.")