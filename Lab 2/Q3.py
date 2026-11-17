weight = float(input("enter wight (kg): "))
height = float(input("enter height (m):"))

bmi = weight/(height**2)

if bmi >= 35:
    print("clinically obese")
elif bmi >= 30:
    print("obese")
elif bmi >= 25:
    print("slightly overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")