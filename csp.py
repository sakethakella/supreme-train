class csp :
    def __init__(self,variables,domain,Rinterference,Rproxy):
        self.variables = variables
        self.domain = domain
        self.Rinterference = Rinterference
        self.Rproxy = Rproxy

    @staticmethod
    def distance(x1,y1,x2,y2):
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def constraints(self):
        hard_constraint=True
        soft_constarint=True
        for i in range(len(self.variables)):
            for j in range(i+1,len(self.variables)):
                if(csp.distance(self.variables[i]['x'],self.variables[i]['y'],self.variables[j]['x'],self.variables[j]['y'])<=self.Rinterference):
                    if(self.variables[i]['f']==self.variables[j]['f']):
                        hard_constraint=False
                        return False
        
        for i in range(len(self.variables)):
            for j in range(i+1,len(self.variables)):
                if(csp.distance(self.variables[i]['x'],self.variables[i]['y'],self.variables[j]['x'],self.variables[j]['y'])<=self.Rproxy):
                    if(abs(self.variables[i]['f']-self.variables[j]['f'])<=1):
                        soft_constarint=False
                        break
        
        return (hard_constraint or soft_constarint)

class csp_solver:
    def __init__(self,csp_problem):
        self.csp_problem = csp_problem
    
    def backtracking(self):
        return 0
    
    def ac3(self):
        return 0
    
    def MRV(self):
        return 0
    
    def LCV(self):
        return 0

    def solution_checker(self):
        constraint_free = self.csp_problem.constraints()
        complete=True
        for i in range(len(self.csp_problem.variables)):
            if(self.csp_problem.variables[i]['f']==0):
                complete=False
                break
        return (constraint_free and complete)
        

base_towers=[{'x':0,'y':0,'f':0},{'x':1,'y':1,'f':0},{'x':2,'y':2,'f':0}]
available_frequencies=[1,2,3,4]

csp_problem = csp(base_towers,available_frequencies,2,2)

print(csp_problem.constraints())