import csp
import search
import utils
import csv

class Problem(csp.CSP):
    
    def __init__(self, semester, courses, professors, difficulty, lab):
        csp.__init__(self, courses)





"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

if __name__=='__main__':

    semester = []
    courses = []
    professors = []
    difficulty = []
    lab = []

    with open('Στοιχεία Μαθημάτων.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if (line_count != 0):
                semester.append(row[0])
                courses.append(row[1])
                professors.append(row[2])
                difficulty.append(row[3])
                lab.append(row[4])
            line_count += 1

    slots = []
    lab_slots = []
    for i in range(1,22):
        new_slot = (i,'9-12')
        slots.append(new_slot)
        lab_slots.append(new_slot)
        new_slot = (i,'12-3')
        slots.append(new_slot)
        lab_slots.append(new_slot)
        new_slot = (i,'3-6')
        slots.append(new_slot)

    dict = {}
    for i in range(len(courses)):
        if lab[i] == "TRUE":
            dict[courses[i]] = lab_slots
        else:
            dict[courses[i]] = slots

    print(dict)
    


    #print("dict ->",dict)

    #problem = Problem(semester,courses,professors,difficulty,lab)
    
    

