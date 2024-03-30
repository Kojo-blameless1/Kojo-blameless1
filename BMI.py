# This program calculates th BMI of a peerson and prints a message
CONST = 703
#Take input for Weight and Height
weight = float(input("Enter Weight in pounds: "))
height = float(input("Enter Your Heigt in inches: "))
BMI = weight * CONST / height**2
#Display message according to conditions
if BMI >= 18.5 and BMI<= 25:
    message = 'You Have optimal weight'
elif BMI < 18.5:
    message = 'You are Under Weight'
else:
    message = 'You are Overweigt'
# Display BMI and message
print(f'BMI: {BMI:,.2f}\n'
    f'{message}')

