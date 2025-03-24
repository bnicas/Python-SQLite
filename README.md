# Python-SQLite
This Python + SQLite project manages student data for Hogwarts School of Witchcraft and Wizardry. It involves importing student information from a CSV file into a database and retrieving class rosters by house using SQL queries.
📁 Project Files
characters.csv: Raw data containing student names, houses, and birth years.

students.db: SQLite database used to store structured student information.

import.py: Script to read and insert student data from the CSV file into the database.

roster.py: Script to display a roster of students from a specified house.

⚙️ Program 1 – import.py
Accepts the name of a CSV file as a command-line argument.

Parses each row, splitting the name field into first, middle (optional), and last names.

Inserts student data into a students table in students.db.

For names with only two parts, the middle field is set to NULL.

📋 Program 2 – roster.py
Accepts a house name as a command-line argument.

Queries the students table for students in that house.

Outputs a neatly formatted class roster:

yaml
Copy
Edit
Hermione Jean Granger, born 1979
Roster is ordered by last name, then first name.

🧠 Key Concepts Practiced
CSV file parsing and data cleaning

SQLite database schema design and population

SQL SELECT queries with WHERE, ORDER BY, and NULL handling

Command-line argument handling in Python

