import streamlit as st

st.title("BMI Calculator")

Height = input("Enter your height in feet: ")
weight = input("Enter your weight in kg: ")
height_in_meters = float(Height) * 0.3048
bmi = (float(weight) / (height_in_meters ** 2))
if bmi < 18.5:
    print("Your BMI is: " + str(bmi)) 
    print("You are Underweight")        
  
if bmi >= 18.5 and bmi <= 24.9:
    print("Your BMI is: " + str(bmi)) 
    print("You are Healthy Weight (Normal)")
if bmi >= 25.0 and bmi <= 29.9:
    print("Your BMI is: " + str(bmi)) 
    print("You are Overweight")
if bmi >= 30.0 and bmi <= 34.9:
    print("Your BMI is: " + str(bmi)) 
    print("You are Obesity (Class 1)")
if bmi >= 35.0 and bmi <= 39.9:
    print("Your BMI is: " + str(bmi)) 
    print("You are Obesity (Class 2)")
if bmi >= 40.0:
    print("Your BMI is: " + str(bmi)) 
    print("You are Severe Obesity (Class 3)")

