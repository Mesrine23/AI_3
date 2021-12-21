import csp
import search
import utils
import csv

class Problem(csp.CSP):
    
    def __init__(self, semester, courses, professors, difficulty, lab):
        self.variables = []
        self.domains = {}
        self.neighbors = {}

        #init variables with courses
        self.variables = courses

        #init domain
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
        dom = {}
        for i in range(len(courses)):
            if lab[i] == "TRUE":
                dom[courses[i]] = lab_slots
            else:
                dom[courses[i]] = slots
        self.domains = dom

        #init neighbors
        neighb = {}
        for nb in range(len(courses)):
            neighbs = []
            for crs in range(len(courses)):
                if(courses[nb]!=courses[crs]):
                    if(semester[nb]==semester[crs]):
                        neighbs.append(courses[crs])
                    elif(professors[nb]==professors[crs]):
                        neighbs.append(courses[crs])
                    elif(difficulty[nb]=="TRUE" and difficulty[crs]=="TRUE"):
                        neighbs.append(courses[crs])
            neighb[courses[nb]] = neighbs
        self.neighbors = neighb
            

        csp.CSP.__init__(self , self.variables , self.domains, self.neighbors, self.var_constrains)


    def var_constrains(A,a,B,b):
        pass



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


    #print("dict ->",dict)

    #problem = Problem(semester,courses,professors,difficulty,lab)
    
    

