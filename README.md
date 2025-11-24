# PythonBMI Calculator Project Details
# Project Title:
BMI Calculator

# Overview of the Project:
This is a simple console-based application written in Python that calculates a person's Body Mass Index (BMI) based on their weight in kilograms (kg) and height in meters (m).  It then provides an interpretation of the BMI result, classifying the user into a standard category such as Underweight, Normal, Overweight, or Obesity. The program includes error handling to ensure that only numeric values are accepted for weight and height inputs.

# Features:
  * BMI Calculation: Accurately computes BMI using the standard formula: $BMI = \frac{weight}{height^2}$.
  * BMI Categorization: Classifies the calculated BMI into one of four standard categories: Underweight, Normal, Overweight, and Obesity.
  * User Input:Prompts the user to enter their weight (kg) and height (m).
  * Output: Displays the calculated BMI value and the corresponding category.
  * Error Handling: Catches ValueError if the user enters non-numeric input.
    
# Technologies/Tools Used:
  * Programming Language: Python 3.x
  * Tools: Standard Python Interpreter (No external libraries required)

# Steps to Install & Run the Project:
1.  Save the Code: Save the provided Python code into a file named bmi_calculator.py.
2.  Open Terminal/Command Prompt: Navigate to the directory where you saved the file using your terminal or command prompt.
3.  Run the Program: Execute the file using the Python interpreter command:
    python bmi_calculator.py
4.  Follow the Prompts: The program will prompt you to enter the required values:
     BMI Calculator
    Enter weight (kg): 
    Enter height (m): 
    
# Instructions for Testing:
Test the program with the following scenarios to verify its functionality and error handling:
| **Test Case** | **Input Weight (kg)** | **Input Height (m)** | **Expected BMI** | **Expected Category** | **Expected Output** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Normal BMI** | 70 | 1.75 | 22.86 | Normal | Your BMI: 22.86, Category: Normal |
| **Underweight** | 50 | 1.70 | 17.30 | Underweight | Your BMI: 17.3, Category: Underweight |
| **Overweight** | 85 | 1.70 | 29.41 | Overweight | Your BMI: 29.41, Category: Overweight |
| **Obesity** | 100 | 1.75 | 32.65 | Obesity | Your BMI: 32.65, Category: Obesity |
| **Invalid Input** | abc`7 | 1.70 | N/A | N/A | Invalid input! Please enter numeric values. |
