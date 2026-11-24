Fitness Data Tracker
Problem Statement No.: 77
Student: Robin Singh
ERP: RU-25-11195
Course: Bachelor of Computer Applications (BCA)
Year: Second Year
Section: BCA-3B
Project Guide: Shushant Sir
Institution: Rungta International Skills University, Bhilai,
Chhattisgarh
About the Project
Fitness Data Tracker is a Python 3 console application for recording
daily step counts and calories burned. It checks progress against a
daily goal of 10,000 steps, provides a summary of recorded activity,
calculates Body Mass Index (BMI), and displays daily step counts in a
Matplotlib bar chart.

The project demonstrates basic Python programming concepts such as
lists, functions, loops, conditional statements, input validation,
calculations, and data visualization.
Features
- Add a daily steps and calories-burned record.
- Check whether the 10,000-step daily goal has been achieved.
- Display the percentage of the daily goal completed.
- Calculate average daily steps.
- Calculate total calories recorded.
- Identify the day with the highest step count.
- Count the number of days on which the step goal was achieved.
- Calculate BMI and display its category.
- Display a bar chart of daily steps with a 10,000-step goal line.
- Reject invalid negative or non-whole-number steps and calorie
  inputs.
Technology Used
  Technology                          Purpose
  Python 3                            Main programming language

  Python lists                        Store step and calorie records
during program execution

  Matplotlib                          Display the daily steps bar chart
Command Prompt / Terminal           Run the application
Project Structure
Fitness-Data-Tracker/
│
├── Folder 1 - Source Code/
│   ├── fitness_tracker.py
│   ├── requirements.txt
│   └── test_cases.txt
│
├── Folder 2 - Project Documentation/
│   ├── Fitness_Tracker_Project_Report.pdf
│   └── Fitness_Tracker_Presentation.pptx
│
└── README.md
Requirements
- Python 3
- Matplotlib
Install the required library from a terminal:
python -m pip install -r "Folder 1 - Source Code/requirements.txt"
How to Run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Install the required package using the command above.
4. Run the Python file:
python "Folder 1 - Source Code/fitness_tracker.py"
If python is not recognized on Windows, try:
py "Folder 1 - Source Code/fitness_tracker.py"
Main Menu
When the program starts, it displays these options:
===== FITNESS DATA TRACKER =====
1. Add Record
2. Summary
3. BMI
4. Chart
0. Exit
Choose an option by entering its menu number.
BMI Calculation
The program calculates BMI using:
BMI = weight in kilograms / (height in metres * height in metres)
The categories used in the assignment are:

  BMI            Category
  Below 18.5     Underweight
18.5 to 24.9   Normal
25 to 29.9     Overweight
30 and above   Obese
Sample Test Scenario
The following sample records are used in the assigned test scenario:

  Day        Steps   Calories
  Day 1      8,000        320
Day 2     12,000        480
Day 3     10,000        400

Expected summary:
- Average steps: 10,000.00
- Total calories: 1,200
- Best day: Day 2 (12,000 steps)
- Goal days: 2/3
BMI example:
- Weight: 70 kg
- Height: 1.75 m
- BMI: 22.86
- Category: Normal
Important Note
The current application stores records in Python lists in memory.
Records are not permanently saved after the program closes.
CSV/database storage and a graphical user interface are possible future
improvements; they are not features of the current version.
Project Documentation
The Folder 2 - Project Documentation folder contains the project
report and presentation.
Acknowledgement
This project was prepared as part of the BCA academic coursework at
Rungta International Skills University under the guidance of Shushant
Sir.
