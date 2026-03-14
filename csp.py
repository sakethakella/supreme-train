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

    
base_towers=[{'x':0,'y':0,'f':0},{'x':1,'y':1,'f':0},{'x':2,'y':2,'f':0}]
available_frequencies=[1,2,3,4]

csp_problem = csp(base_towers,available_frequencies,2,2)

print(csp_problem.constraints())