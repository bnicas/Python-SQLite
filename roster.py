import sys
import csv
from cs50 import SQL

# Check for correct number of args
if len(sys.argv) != 2:
    print("Usage: roster.py house")
    sys.exit(1)

house_arg = sys.argv[1]

db = SQL("sqlite:///students.db")

# select all rows from the table and order by last and then first name
student_DB = db.execute("SELECT first, middle, last, house, birth FROM students ORDER BY last, first")

# for each row create a list of keys and values
for row in student_DB:
    keys = []
    values = []
    items = row.items()

    for item in items:
        keys.append(item[0]), values.append(item[1])

    # check for house and NULL values for middle names and then print full name and birth year
    if (house_arg == values[3] and values[1] == None):
        print(values[0], values[2] + ",", "born", values[4])
    elif(house_arg == values[3] and values[1] != None):
        print(values[0], values[1], values[2]+",", "born", values[4])
