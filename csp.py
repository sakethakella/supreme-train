from queue import Queue

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
                if(self.variables[i]['f']!=0 and self.variables[j]['f']!=0):
                    if(csp.distance(self.variables[i]['x'],self.variables[i]['y'],self.variables[j]['x'],self.variables[j]['y'])<=self.Rinterference and self.variables[i]['f']==self.variables[j]['f']):
                        hard_constraint=False
                        return False
        
        for i in range(len(self.variables)):
            for j in range(i+1,len(self.variables)):
                if(self.variables[i]['f']!=0 and self.variables[j]['f']!=0):
                    if(csp.distance(self.variables[i]['x'],self.variables[i]['y'],self.variables[j]['x'],self.variables[j]['y'])<=self.Rproxy and abs(self.variables[i]['f']-self.variables[j]['f'])<=1):
                        soft_constarint=False
                        break
        return (hard_constraint or soft_constarint)

class csp_solver:
    def __init__(self,csp_problem):
        self.csp_problem = csp_problem
    
    def backtracking(self):
        if all(v['f'] != 0 for v in self.csp_problem.variables):
            return True
        for i in range(len(self.csp_problem.variables)):
            if self.csp_problem.variables[i]['f'] == 0:
                for f in self.csp_problem.domain[i]:
                    self.csp_problem.variables[i]['f'] = f
                    if self.csp_problem.constraints():
                        #ac3 arc consstancy needs to used here
                        self.ac3()
                        if self.backtracking():
                            return True
                    self.csp_problem.variables[i]['f'] = 0
                return False
    
    def ac3(self):
        q=Queue()
        for i in range(len(self.csp_problem.variables)):
            for j in range(i,len(self.csp_problem.variables)):
                if(i!=j):
                    q.put((i,j))
        while(not q.empty()):
            (i,j)=q.get()
            for f in list(self.csp_problem.domain[i]):
                supported = False
                temp1=self.csp_problem.variables[i]['f']
                temp2=self.csp_problem.variables[j]['f']
                for g in self.csp_problem.domain[j]:
                    self.csp_problem.variables[i]['f'] = f
                    self.csp_problem.variables[j]['f'] = g
                    if self.csp_problem.constraints():
                        supported = True
                        break
                self.csp_problem.variables[j]['f'] = temp2
                self.csp_problem.variables[i]['f'] = temp1
                if not supported:
                    self.csp_problem.domain[i].remove(f)

        print(self.csp_problem.domain)
        print("AC3 done")

    
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
available_frequencies=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]

csp_problem = csp(base_towers,available_frequencies,2,2)
csp_solver_instance=csp_solver(csp_problem)

print(csp_problem.constraints())
print(csp_solver_instance.backtracking())
print(csp_problem.variables)
print(csp_solver_instance.solution_checker())
