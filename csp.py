from queue import Queue
import copy

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
        for i in range(len(self.variables)):
            for j in range(i+1,len(self.variables)):
                if(self.variables[i]['f']!=0 and self.variables[j]['f']!=0):
                    if(csp.distance(self.variables[i]['x'],self.variables[i]['y'],self.variables[j]['x'],self.variables[j]['y'])<=self.Rinterference and self.variables[i]['f']==self.variables[j]['f']):
                        return False
        
        for i in range(len(self.variables)):
            for j in range(i+1,len(self.variables)):
                if(self.variables[i]['f']!=0 and self.variables[j]['f']!=0):
                    if(csp.distance(self.variables[i]['x'],self.variables[i]['y'],self.variables[j]['x'],self.variables[j]['y'])<=self.Rproxy and abs(self.variables[i]['f']-self.variables[j]['f'])<=1):
                        return False
                        
        return True


class csp_solver:
    def __init__(self,csp_problem):
        self.csp_problem = csp_problem
    
    def backtracking(self):
        if all(v['f'] != 0 for v in self.csp_problem.variables):
            return True
        i=self.MRV()
        for f in self.LCV(i):
            self.csp_problem.variables[i]['f'] = f
            if self.csp_problem.constraints():
                backup = copy.deepcopy(self.csp_problem.domain)
                if self.ac3():
                    result = self.backtracking()
                else:
                    result = False
                self.csp_problem.domain = backup
                if result:
                    return True
            self.csp_problem.variables[i]['f'] = 0 
        return False
    
    def ac3(self):
        q=Queue()
        for i in range(len(self.csp_problem.variables)):
            for j in range(len(self.csp_problem.variables)):
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
                    if len(self.csp_problem.domain[i]) == 0:
                        return False

                    for k in range(len(self.csp_problem.variables)):
                        if k != i and k != j:
                            q.put((k,i))

        return True

    def MRV(self):
        min_domain=float('inf')
        min_index=-1
        for i in range(len(self.csp_problem.domain)):
            k=len(self.csp_problem.domain[i])
            if(k<min_domain and self.csp_problem.variables[i]['f']==0):
                min_domain=k
                min_index=i
        return min_index  

    def LCV(self,i):

        values = []

        for v in self.csp_problem.domain[i]:

            removed = 0

            for j in range(len(self.csp_problem.variables)):

                if j == i:
                    continue

                for g in self.csp_problem.domain[j]:
                    temp1 = self.csp_problem.variables[i]['f']
                    temp2 = self.csp_problem.variables[j]['f']
                    self.csp_problem.variables[i]['f'] = v
                    self.csp_problem.variables[j]['f'] = g
                    if not self.csp_problem.constraints():
                        removed += 1
                    self.csp_problem.variables[i]['f'] = temp1
                    self.csp_problem.variables[j]['f'] = temp2

            values.append((removed, v))
        values.sort()
        return [v for _, v in values]

    def solution_checker(self):
        constraint_free = self.csp_problem.constraints()
        complete=True
        for i in range(len(self.csp_problem.variables)):
            if(self.csp_problem.variables[i]['f']==0):
                complete=False
                break
        return (constraint_free and complete)
        

base_towers=[{'x':0,'y':0,'f':0},{'x':1,'y':0,'f':0},{'x':2,'y':0,'f':0},{'x':0,'y':1,'f':0},{'x':1,'y':1,'f':0},{'x':2,'y':1,'f':0},{'x':0,'y':2,'f':0},{'x':1,'y':2,'f':0},{'x':2,'y':2,'f':0}]
Rint=2
Rprox=2
k=1
while True: 
    freq=[]
    for i in range(k):
        freq.append(i+1)
    available_frequencies=[list(freq) for i in range(len(base_towers))]
    csp_problem = csp(base_towers,available_frequencies,Rint,Rprox)
    csp_solver_instance=csp_solver(csp_problem)
    if(csp_solver_instance.backtracking()):
        print("solution found")
        print(csp_problem.variables)
        break
    k=k+1
    
