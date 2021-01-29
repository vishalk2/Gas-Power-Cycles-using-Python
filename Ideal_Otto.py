import matplotlib.pyplot as plt
import numpy as np
from sympy import *

class IdealOtto:
    
    def __init__(self,r=8,k=1.4,R=0.287,Cv=0.718):
        print('Ideal Otto Cycle')
        print('----------------')
        print()
        print('SI Units to be followed:')
        print('---------------------------------------------------------------------------------------------------')
        print('|            Entity               | Symbol(s) used |  Units  |          Units in brief            |')
        print('|-------------------------------------------------------------------------------------------------|')
        print('|           Pressures             | [P1,P2,P3,P4]  |  kPa    |           Kilo Pascal              |')
        print('|         Temperatures            | [T1,T2,T3,T4]  |  K      |             Kelvin                 |')
        print('|       Specific Volumes          | [v1,v2,v3,v4]  |  m^3    |           Cubic metres             |')
        print('|        Heat addition            |      q_in      |  kJ/kg  |       Kilo Joule per Kilogram      |')
        print('|        Heat rejection           |      q_out     |  kJ/kg  |       Kilo Joule per Kilogram      |')
        print('|          Work Output            |      w_net     |  kJ/kg  |       Kilo Joule per Kilogram      |')
        print('|          Efficiency             |      eta       |   NA    |          Dimensionless             |')
        print('|      Compression Ratio          |       r        |   NA    |          Dimensionless             |')
        print('| Specific Heat @ Constant Volume |       Cv       |  kJ/kgK | Kilo Joule per Kelvin per Kilogram |')
        print('|         Gas Constant            |       R        |  kJ/kgK | Kilo Joule per Kelvin per Kilogram |')
        print('---------------------------------------------------------------------------------------------------')
        print()
        #Defining default values for r, R, Cv and k
        self.r = r
        self.k = k
        self.R = R
        self.Cv = Cv
        print('______________________________________________________________________________________________________________')
        print('|   Executable Component    |  Component Type  |                          Utility                            |')
        print('|___________________________|__________________|_____________________________________________________________|')
        print('|                           |                  |  -> Allows to define a state with P, T & v values.          |') 
        print('|                           |                  |     {P - Pressure ; T - Temperature ; v - Specific Volume}  |')
        print('|                           |                  |  -> Input format (default : "unknown" for all 4 variables)- |')
        print('| define_state(state,P,T,v) |      Method      |     state : An integer in the range[1,4] both inclusive     |')
        print('|                           |                  |     P     : Float or Integer if known else Symbol wrt state |')
        print('|                           |                  |     T     : Float or Integer if known else Symbol wrt state |')
        print('|                           |                  |     v     : Float or Integer if known else Symbol wrt state |')
        print('|---------------------------|------------------|-------------------------------------------------------------|')
        print('|                           |                  |  -> Allows to add heat addition value.                      |')
        print('|                           |                  |     {q_in - Specific Heat Addition}                         |')
        print('|  add_heat_addition(q_in)  |      Method      |  -> Input format (default set to "unknown")-                |')
        print('|                           |                  |     q_in  : Float or Integer if known else Symbol           |')
        print('|---------------------------|------------------|-------------------------------------------------------------|')
        print('|                           |                  |  -> Allows to add heat rejection value.                     |')
        print('|                           |                  |     {q_out - Specific Heat Rejection}                       |')
        print('| add_heat_rejection(q_out) |      Method      |  -> Input format (default set to "unknown")-                |')
        print('|                           |                  |     q_out  : Float or Integer if known else Symbol          |')
        print('|---------------------------|------------------|-------------------------------------------------------------|')
        print('|                           |                  |  -> Allows to add work output value.                        |')
        print('|                           |                  |     {w_net - Net Specific Work Output}                      |')
        print('|  add_work_output(w_net)   |      Method      |  -> Input format (default set to "unknown")-                |')
        print('|                           |                  |     w_net  : Float or Integer if known else Symbol          |')
        print('|---------------------------|------------------|-------------------------------------------------------------|')
        print('|                           |                  |  -> Allows to add efficiency value.                         |')
        print('|                           |                  |     {eta - Efficiency of the Engine}                        |')
        print('|  add_efficiency(eta)      |      Method      |  -> Input format (default set to "unknown")-                |')
        print('|                           |                  |     eta  : Float or Integer if known else Symbol            |')
        print('|---------------------------|------------------|-------------------------------------------------------------|')
        print('|                           |                  |  -> Performs the analytical task of the problem statement   |')
        print('|                           |                  |     using CASA. {CASA - Cold air standard assumptions}      |')
        print('|   analysis_using_CASA()   |      Method      |  -> No input required.                                      |')
        print('|                           |                  |  -> Concludes with a message "Analysis Complete".           |')
        print('|---------------------------|------------------|-------------------------------------------------------------|')
        print('|                           |                  |  -> Enables to view values of Pressures, Temperatures, and  |')
        print('|      state_variables      |     Attribute    |     Specific Volumes in respective states.                  |')
        print('|                           |                  |  -> Returns a dictionary with respective parameters.        |')
        print('|---------------------------|------------------|-------------------------------------------------------------|')
        print('|                           |                  |  -> Enables to view values of q_in, q_out and w_net.        |')
        print('|       path_variables      |     Attribute    |  -> Returns a dictionary with respective parameters.        |')
        print('|                           |                  |                                                             |')
        print('|---------------------------|------------------|-------------------------------------------------------------|')
        print('|                           |                  |  -> Displays the analytical value of efficiency (eta).      |')
        print('|        efficiency         |     Attribute    |  -> Outputs a float value of efficiency.                    |')
        print('|                           |                  |                                                             |')
        print('|---------------------------|------------------|-------------------------------------------------------------|')
        print('|                           |                  |  -> Enables to calculate Efficiency without executing any   |')
        print('|                           |                  |     other commands.                                         |')
        print('|   get_efficiency(new_r)   |      Method      |  -> Uses CASA (takes in value for compression ratio).       |')
        print('|                           |                  |  -> Input format (default value set to 8)-                  |')
        print('|                           |                  |     new_r : Integer                                         |')
        print('|---------------------------|------------------|-------------------------------------------------------------|')
        print('|           r               |     Attribute    |  -> Displays the Compression ratio value (Default set to 8) |')
        print('|---------------------------|------------------|-------------------------------------------------------------|')
        print('|           k               |     Attribute    |  -> Displays Specific heat ratio value (default set t0 1.4) |')
        print('|---------------------------|------------------|-------------------------------------------------------------|')
        print('|           Cv              |     Attribute    |  -> Displays Specific Heat @ Constant Volume(Default=0.718) |')
        print('|---------------------------|------------------|-------------------------------------------------------------|')
        print('|           R               |     Attribute    |  -> Displays Gas constant value (Default set to 0.287)      |')
        print('|___________________________|__________________|_____________________________________________________________|')
        print()
        print('Default Values')
        print({'Compression Ratio':self.r, 'Specific Heat Ratio':self.k, 
               'Gas Constant':self.R,'Constant volume specific heat':self.Cv})
        #Defining state_variables for P,T and v
        self.state_variables = {'State-1':{'P1':'unknown','T1':'unknown','v1':'unknown'},
                                'State-2':{'P2':'unknown','T2':'unknown','v2':'unknown'},
                                'State-3':{'P3':'unknown','T3':'unknown','v3':'unknown'},
                                'State-4':{'P4':'unknown','T4':'unknown','v4':'unknown'},
                               'Mean_effective_pressure':'unknown'}
        #Defining path_variables for taking q_in,q_out and w_net
        self.path_variables = {'q_in':'unknown','q_out':'unknown','w_net':'unknown'}
        self.efficiency = 'unknown' #Defining efficiency for assigning it to eta
            
    def define_state(self,state,P='unknown',T='unknown',v='unknown'):
        self.state_variables['State-'+str(state)[-1]]['P'+str(state)[-1]] = P
        self.state_variables['State-'+str(state)[-1]]['T'+str(state)[-1]] = T
        self.state_variables['State-'+str(state)[-1]]['v'+str(state)[-1]] = v

    def add_heat_addition(self,q_in='unknown'):
        self.path_variables['q_in'] = q_in
        
    def add_heat_rejection(self,q_out='unknown'):
        self.path_variables['q_out'] = q_out
        
    def add_work_output(self,w_net='unknown'):
        self.path_variables['w_net'] = w_net
        
    def add_efficiency(self,eta='unknown'):
        self.efficiency = eta
        
    def get_efficiency(self,new_r=8):
        eta = 1-(1/pow(new_r,self.k-1))
        print('According to Cold Air-Standard Assumptions -')
        print('For Compression ratio = {},'.format(new_r))
        print('Efficiency of the Otto Cycle is {} i.e {}%'.format(round(float(eta),4),round(float(eta)*100,2)))
        
    def analysis_using_CASA(self):
        #CASA - Cold Air Standard Assumptions
        vl = [] #vl - variable list
        for i in range(1,5):
            for j in self.state_variables['State-'+str(i)].values():
                vl.append(j)
        for i in self.path_variables.values():
            vl.append(i)
        vl.append(self.efficiency)
        # Taking all variables and constants within vl (variable list) and then assigning them respectively as below.
        P1,T1,v1,P2,T2,v2,P3,T3,v3,P4,T4,v4,q_in,q_out,w_net,eta = vl
        
        t = tuple([i for i in vl if not isinstance(i,(int,float))]) #Taking only symbolic variables inside the tuple
        
        #Equations for solving
        eq1 = Eq(T2,T1*pow(self.r,self.k-1))
        eq2 = Eq(P2,P1*pow(self.r,self.k))
        eq3 = Eq(self.Cv*(T3-T2),q_in)
        eq4 = Eq(T3,T4*pow(self.r,self.k-1))
        eq5 = Eq(P3*T2,P2*T3)
        eq6 = Eq(P4*T1,P1*T4)
        eq7 = Eq(self.Cv*(T4-T1),q_out)
        eq8 = Eq(q_in-q_out,w_net)
        eq9 = Eq(eta,w_net/q_in)
        eq10 = Eq(P1*v1,self.R*T1)
        eq11 = Eq(v1,self.r*v2)
        eq12 = Eq(v4,v1)
        eq13 = Eq(v3,v2)
        
        #Using solve() from Sympy to solve simultaneous equations
        sol = solve((eq4,eq3,eq7,eq1,eq5,eq6,eq2,eq9,eq8,eq10,eq11,eq12,eq13),t,dict=True)
        
        #Assigning final values for respective variables
        for i in range(1,5):
            if(self.state_variables['State-'+str(i)]['P'+str(i)] in sol[0]):
                self.state_variables['State-'+str(i)]['P'+str(i)] = round(float(sol[0][self.state_variables['State-'+str(i)]['P'+str(i)]]),3)
            if(self.state_variables['State-'+str(i)]['T'+str(i)] in sol[0]):
                self.state_variables['State-'+str(i)]['T'+str(i)] = round(float(sol[0][self.state_variables['State-'+str(i)]['T'+str(i)]]),3)
            if(self.state_variables['State-'+str(i)]['v'+str(i)] in sol[0]):
                self.state_variables['State-'+str(i)]['v'+str(i)] = round(float(sol[0][self.state_variables['State-'+str(i)]['v'+str(i)]]),3)
        
        if(self.path_variables['q_in'] in sol[0]):
            self.path_variables['q_in'] = round(float(sol[0][q_in]),3)
        if(self.path_variables['q_out'] in sol[0]):
            self.path_variables['q_out'] = round(float(sol[0][q_out]),3)
        if(self.path_variables['w_net'] in sol[0]):
            self.path_variables['w_net'] = round(float(sol[0][w_net]),3)
        
        self.efficiency = round(float(sol[0][eta]),5)
        self.state_variables['Mean_effective_pressure'] = self.path_variables['w_net']/(self.state_variables['State-1']['v1']-self.state_variables['State-2']['v2'])
        
        #Plotting P-V Diagram
        Y1 = self.state_variables['State-1']['P1']
        X1 = self.state_variables['State-1']['v1']
        Y2 = self.state_variables['State-2']['P2']
        X2 = self.state_variables['State-2']['v2']
        Y3 = self.state_variables['State-3']['P3']
        X3 = self.state_variables['State-3']['v3']
        Y4 = self.state_variables['State-4']['P4']
        X4 = self.state_variables['State-4']['v4']
        
        c1 = Y1*pow(X1,self.k)
        c2 = Y3*pow(X3,self.k)
        
        #Isentropic Compression
        x1 = np.linspace(X1,X2,num=50)
        y1 = c1/pow(x1,self.k)
        
        #Constant Volume Heat Addition
        y2 = np.linspace(y1[-1],Y3,num=50)
        x2 = np.array([x1[-1] for i in range(50)])
        
        #Isentropic Expansion
        x3 = np.linspace(X3,X4,num=50)
        y3 = c2/pow(x3,self.k)
        
        #Constant Volume heat Rejection
        y4 = np.linspace(y3[-1],Y1,num=50)
        x4 = np.array([x3[-1] for i in range(50)])
        
        plt.plot(x1,y1,label='Isentropic Compression')
        plt.plot(x2,y2,label='Constant Volume Heat Addition')
        plt.plot(x3,y3,label='Isentropic Expansion')
        plt.plot(x4,y4,label='Constant Volume Heat Rejection')
        plt.xlabel('Specific Volume'),plt.ylabel('Pressure'),plt.title('P-V diagram of Ideal Otto Cycle')
        plt.legend()
        
        print('Analysis Complete')
        print('Execute state_variables, path_variables and efficiency for final values')
