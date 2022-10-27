#BMI Calculator
#Taking in values
height = input("what is your height in m?\n")
weight = input("what is your weight in kg?\n")
#checking types of data
print(type(height))
new_height = float(height)
print(type(new_height))
new_weight = int(weight)
#BMI Calculation
BMI = new_weight / new_height ** 2
#BMI Conversion
BMI_int = int(BMI)
new_BMI = str(BMI_int)
print("your BMI is " + new_BMI + " kg/m*m")