import sys
import csv
from cs50 import SQL

# Check for correct number of args
if len(sys.argv) != 2:
    print("Usage: import.py characters.csv")
    sys.exit(1)

db = SQL("sqlite:///students.db")
# read a csv file as list
with open(sys.argv[1], 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=",")
    # for each row create a list of keys and values
    for row in csv_reader:
        keys = []
        values = []
        items = row.items()

        for item in items:
            keys.append(item[0]), values.append(item[1])

        # split name into a list of first name, middle name and last name
        names = values[0].split()

        # Insert each student into the students table of students.db
        if (len(names)) == 3:

            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                       (names[0], names[1], names[2], values[1], values[2]))

        else:

            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                       (names[0], None, names[1], values[1], values[2]))

