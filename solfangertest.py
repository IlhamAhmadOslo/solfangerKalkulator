# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 08:41:36 2020

@author: Eier
"""

import pandas as pd
F= pd.read_csv("C:/Users/Eier/.spyder-py3/Måledata_mars_juli_2020.csv")
Straaling = F[F['Irradiance (W/m2)'] > 790  ]
Straaling = Straaling.set_index('Time')
Straaling.reset_index(inplace= True)
Straaling['Time']= pd.to_datetime(Straaling.Time)
Straaling['minute']=Straaling['Time'].dt.minute

S = Straaling.values.tolist()
                    

k=[]
t = 0
i = 0
#tidsserier = []
while i < len(S)-1:
    if S[i][6]- S[i+1][6] == -1 and S[i+1][6]- S[i][6] == 1:
        k.extend([S[i],S[i+1]])
        
        
        t += 1
    
    i += 1
    t = 0   

endelig=[]
for x in k:
    if x not in endelig:
        endelig.append(x)

"""    
k=[]
t = 0
i = 0
tidsserier = []
while t<=15:
    
    while i < len(S)-1:
        if S[i][6]- S[i+1][6] == -1 and S[i+1][6]- S[i][6] == 1:
            k.extend([S[i],S[i+1]])
            for x in k:
                if x not in endelig:
                    endelig.append(x)
                    if x[t][6]+x[i+1][6] >= 15:
                        tidsserier.extend([x[t],x[i+1]])
        
        
        t += 1
    
    i += 1
     

"""
from pandas import DataFrame
#your_list = ['Time', 'Irradiance (W/m2)', 'Ambient Temperature (C)','Inlet Temperature (C)','Mass flow (g/s)','Outlet Temperature (C)','min']
df = DataFrame (endelig,columns=['Time', 'Irradiance (W/m2)', 'Ambient Temperature (C)','Inlet Temperature (C)','Mass flow (g/s)','Outlet Temperature (C)','min'])
df['valg']=df['Time'].dt.to_period('H')  
g= df.groupby('valg')
r=[]
for tid, info in g:
    r.append(info)

    
sor_tid=[]

for i in range(len(r)):
    if len(r[i]) >= 15:
        sor_tid.append(r[i])
        
for i in sor_tid:
    
    i= i.set_index('Time')
 
    
for o in sor_tid:
    
     o.values.tolist()    
"""t=0
OK=[]   
for i in sor_tid:
    while t < len(i)-1:
        if i['min'][t]- i['min'][t+1]:
            OK.extend([i['min'][t],i['min'][t+1]])
            
        t +=1
        
        
endelig=[]
for x in k:
    if x not in endelig:
        endelig.append(x)  
 """       
        
 
        
import numpy as np
x= np.array([2, 6 , 8 ,111])
 
t=np.zeros((2,4))     
    
 
for i in yearly_sales_1.index:
    a = yearly_sales_1['north_america_sales'][i]
    for j in yearly_sales_1.index:
        if i==j:
            break
        else:
            continue
            #b=sum(a)
    
        print(a)