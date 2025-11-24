# Problem Statement:
The primary problem addressed by this project is the need for a simple, quick, and automated method to calculate a person's Body Mass Index (BMI) using their weight and height, and subsequently classify this BMI into a standard health category .
Manually calculating BMI is error-prone and slow, and this program provides a digital solution for this basic health metric assessment.

# Scope of the Project:
The project's scope is limited to the calculation and categorization of BMI** based on user-provided weight (in kilograms) and height (in meters).
* Inclusions-
    * Accepting numeric input for weight and height.
    * Calculating BMI using the formula: $BMI = \frac{weight}{height^2}$.
    * Categorizing the resulting BMI into one of four standard groups (Underweight, Normal, Overweight, Obesity).
    * Handling potential ValueError exceptions for non-numeric input.
* Exclusions-
    * Data storage or user profile management.
    * Detailed health recommendations or medical advice.
    * Support for different measurement units (e.g., pounds and feet/inches).
    * Graphical User Interface (GUI); it operates solely as a Command-Line Interface (CLI) application.
      
# Target Users:
The program targets **any individual or professional who needs a quick and simple calculation of BMI.

* General Users: Individuals who want to monitor their own health or fitness progress.
* Fitness Enthusiasts: People tracking their body composition goals.
* Healthcare/Wellness Professionals: Dietitians, fitness trainers, or nurses who need to quickly calculate a patient's or client's BMI as a preliminary screening tool.
  
# High-Level Features:
* BMI Calculation: A dedicated function (calculate_bmi) to accurately compute the BMI value from weight and height inputs.
* BMI Classification: A dedicated function (bmi_category) to classify the calculated BMI into standard health categories: Underweight ( $< 18.5$), Normal ($18.5 - 24.9$), Overweight ($25.0 - 29.9$), and Obesity ($30.0+$).
* Input Validation: Robust error handling using a try except ValueError block to ensure the user inputs are valid numeric values.
* User Interface: A simple and clear Command-Line Interface (CLI) for prompting input and displaying results.
