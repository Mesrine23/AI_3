import csp
#import search
#import utils
import csv
import sys
import time

class Timetabling(csp.CSP):
    
    def __init__(self, semester, courses, professor, difficulty, lab):
        self.variables = []
        self.domains = {}
        self.neighbors = {}


        self.semesters = semester
        self.professors = professor
        self.difficulties = difficulty
        self.labs = lab
        self.constraints_counter = 0

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
                        neighbs.append(courses[crs])
            neighb[courses[nb]] = neighbs
        self.neighbors = neighb

        #init neighbors in constraints as a list of tuples -> [(a1,b1),(a2,b2),...]
        #for dom/wdeg
        constrained_neighbors = []
        for variable in self.variables:
            for neighbor in self.neighbors:
                if(variable!=neighbor):
                    constrained_neighbors.append((variable,neighbor))

        csp.CSP.__init__(self , self.variables , self.domains, self.neighbors, self.var_constraints, constrained_neighbors)


    def var_constraints(self,A,a,B,b):
        self.constraints_counter += 1
        #oxi idia mera & idia wra OR idio mathima
        if (a==b or A==B): 
            return False
         
        #oxi idio etos-eksamino sthn idia mera
        if(a[0]==b[0]): #idia mera
            courseA=-1
            courseB=-1
            for i in range(len(self.variables)):
                if(self.variables[i]==A):
                    courseA = i
                if(self.variables[i]==B):
                    courseB = i
                if(courseA!=-1 and courseB!=-1):
                    break
            if(self.semesters[courseA]==self.semesters[courseB]): #idio etos
                return False
        
        #keno 2 hmerwn anamesa se 2 duskola mathimata
        if(abs(a[0]-b[0])<2): #ligotero apo 2 meres diafora
            courseA=-1
            courseB=-1
            for i in range(len(self.variables)):
                if(self.variables[i]==A):
                    courseA = i
                if(self.variables[i]==B):
                    courseB = i
                if(courseA!=-1 and courseB!=-1):
                    break
            if(self.difficulties[courseA]=="TRUE" and self.difficulties[courseB]=="TRUE"): #an einai kai ta 2 duskola mathimata
                return False
        
        #oxi idios kathigitis thn idia mera
        if(a[0]==b[0]): #idia mera
            courseA=-1
            courseB=-1
            for i in range(len(self.variables)):
                if(self.variables[i]==A):
                    courseA = i
                if(self.variables[i]==B):
                    courseB = i
                if(courseA!=-1 and courseB!=-1):
                    break
            if(self.professors[courseA]==self.professors[courseB]): #an einai kai ta 2 duskola mathimata
                return False
        
        #provlima me ergasthrio
        if(a[0]==b[0]):
            courseA=-1
            courseB=-1
            for i in range(len(self.variables)):
                if(self.variables[i]==A):
                    courseA = i
                if(self.variables[i]==B):
                    courseB = i
                if(courseA!=-1 and courseB!=-1):
                    break
            if(self.labs[courseA]=="TRUE" and self.labs[courseB]=="TRUE"): #kai ta 2 ergasthrio
                return False
            elif(self.labs[courseA]=="TRUE"): #mono to ena apo ta 2
                if( (a[1]=="9-12" and b[1]=="12-3") or (a[1]=="12-3" and b[1]=="3-6") ):
                    return False
            elif(self.labs[courseB]=="TRUE"):
                if( (b[1]=="9-12" and a[1]=="12-3") or (b[1]=="12-3" and a[1]=="3-6") ):
                    return False

        return True



"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

if __name__=='__main__':

    semester = []
    courses = []
    professors = []
    difficulty = []
    lab = []

    with open('???????????????? ??????????????????.csv',encoding="utf8") as csv_file:
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


    problem = Timetabling(semester,courses,professors,difficulty,lab)

    #csp.backtracking_search(problem, csp.mrv, csp.lcv, csp.mac)
    
    #csp.backtracking_search(problem, csp.mrv, csp.lcv, csp.forward_checking)

    #csp.backtracking_search(problem, csp.dom_wdeg, csp.lcv, csp.mac)

    #csp.backtracking_search(problem, csp.dom_wdeg, csp.lcv, csp.forward_checking)

    """
    print("\nElapsed time: ", end-start)
    print("nassigns: ",problem.nassigns)
    print("constraints_counter: ",problem.constraints_counter)
    """

    #problem.display(problem.infer_assignment())
    
    
    out = csp.min_conflicts(problem)
    #print(out)
    end = time.time() #ending time elapsed
    """
    print("\nElapsed time: ", end-start)
    print("nassigns: ",problem.nassigns)
    print("constraints_counter: ",problem.constraints_counter)
    """