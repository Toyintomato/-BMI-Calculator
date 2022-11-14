#BMI Calculator
#Taking in values
height = float(input("what is your height in m?\n"))
weight = float(input("what is your weight in kg?\n"))
if weight < 18.5:
  print("You are under weight.")
elif weight >= 18.5 and weight < 25:
  print("You have a normal weight.")
elif weight >= 25 and weight < 30:
  print("You are over weight.")
elif weight >= 30 and weight < 35:
  print("You are obese.")
elif weight >= 35:
  print("You are clinically obese.")
#BMI Calculation
BMI = round((weight / height ** 2), 2)
print(f"your BMI is {BMI}kg/m*m")