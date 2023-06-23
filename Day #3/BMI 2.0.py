print("\033c")

weight = int(input("Enter Weight\n (kg):"))
height = float(input("Enter Height\n (m):"))

bmi = weight / height **2
bmi = round(bmi)


if bmi > 5 and bmi < 18.5 :
    print(f"your BMI is {bmi}, You're Underweight")
elif bmi >18.5 and bmi < 25:
    print(f"your BMI is {bmi}, You have a Normal Weight")
elif bmi > 25 and bmi < 30:
    print(f"your BMI is {bmi}, You're a slightly Overweight")
elif bmi >30 and bmi < 35:
    print(f"your BMI is {bmi}, You're Obese")
elif bmi > 35:
    print(f"your BMI is {bmi}, You're Clinicaly Obese")
else:
    print("input not supported")