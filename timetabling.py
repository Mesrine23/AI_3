import csp
import search
import utils
import csv

semester = []
variables = []
professors = []
difficulty = []
laboratory = []

with open('Στοιχεία Μαθημάτων.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if (line_count != 0):
            semester.append(row[0])
            variables.append(row[1])
            professors.append(row[2])
            difficulty.append(row[3])
            laboratory.append(row[4])
        line_count += 1

for count in range(0,line_count-1):
    print(semester[count],variables[count],professors[count],difficulty[count],laboratory[count])
    

