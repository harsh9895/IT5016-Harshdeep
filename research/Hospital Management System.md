Hospital Management System
Overview
This Hospital Management System is a simple text-based application developed in Python using Object-Oriented Programming (OOP) principles. It allows users to manage doctors and patients, providing functionalities to admit and discharge patients, treat them, and list current patients and doctors.

Features
Add doctors with name and specialty
Admit patients with name and age
Discharge patients
Treat patients by doctors
List all admitted patients and available doctors
Software Design Principles
KISS (Keep It Simple, Stupid)
Simplicity in Design: The code follows the KISS principle by maintaining a straightforward structure. Each class has a clear and single responsibility (e.g., Patient, Doctor, and Hospital), making it easy to understand and maintain.
User Interaction: The menu-driven interface is intuitive, guiding users through available options without overwhelming them with complexity.
DRY (Don't Repeat Yourself)
Avoiding Redundancy: The code minimizes redundancy by encapsulating functionalities within classes. For instance, patient admission and discharge logic is centralized in the Patient class, avoiding duplication of code across the application.
Reusability: Methods within classes are designed for reuse. For example, the treat method in the Doctor class checks patient admission status, promoting code reuse and reducing the chances of errors.
Installation
Ensure you have Python installed on your system (version 3.6 or higher).
Copy the provided code into a .py file (e.g., hospital_management.py).
Run the program using the command:
bash
Copy code
python hospital_management.py
Usage
Follow the on-screen prompts to add doctors and patients.
Use the menu options to manage patients and doctors as needed.
To exit the application, select the exit option from the menu.
Future Improvements
Implement a database for persistent storage of patients and doctors.
Add user authentication to secure access to the system.
Enhance the user interface with a graphical UI.