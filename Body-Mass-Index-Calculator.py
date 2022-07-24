# Author: Parsa Ahmadnezhad
# BMI Calculator

print("Welcome to BMI Calculator!")
print("This tool gives your BMI (body mass index) to help you have more information about your body mass.")
print("BMI Chart:")
print("Below 18.5 : UNDERWEIGHT")
print("18.5 - 24.9: HEALTHY")
print("25.0 - 30.0: OVERWEIGHT ")
print("Above 30 : OBESE")
print("You will need to enter your weight (lb) and your height (inch).")

weight = float(input("Weight (lb): "))
height = float(input("Height (inch): "))
bmi = round(weight / (height ** 2) * 703,1)

if bmi < 18.5:
    bmiFeedback = "Your BMI is " + str(bmi) + ". You might want to start eating more calories. Low BMI can lead to a lot of health risks."
elif 18.5 <= bmi <= 24.9:
    bmiFeedback = "Your BMI is " + str(bmi) + ". You have a healthy BMI. Keep it up!"
elif 25 <= bmi <= 30:
    bmiFeedback = "Your BMI is " + str(bmi) + ". Your BMI is a bit high, you could eat less calories and do more activites throughout the day to be more healthy."
elif bmi > 30:
        bmiFeedback = "Your BMI is " + str(bmi) + ". You should really start to do more exercise and eat more fruit & vegetables "

print(bmiFeedback)
print("Thank you for using our program!")
