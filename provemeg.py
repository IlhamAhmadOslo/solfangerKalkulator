# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:55:02 2020

@author: Eier
"""

import pandas as pd
fil= pd.read_csv("C:/Users/Eier/Downloads/Måledata_LAB 6_MaiAugust2020.csv")

""" energi som ble lagret i brønnparken for hele perioden"""
T_inn= fil['TE1003']
T_ut= fil['TE0004']
M_V= fil['FE1200']
M_O= fil['FE1100']


m_s= M_V + M_O
m_strom= (m_s)/(10**3)
C_p= 4183
E_Parken=[]
for i in range(len(fil)):
    
    Q= m_strom[i]*C_p*(T_inn[i]-T_ut[i])*60
    E_Parken.append(Q)
 
Q_Parken=sum(E_Parken)

# Energi lagret i bakken gjennom perioden (i kWh):
#Lagret_tot =Q_Parken/(1000*3600)


 #den totale mengde energi instrålt på fangarne hele perioden

t=fil['RE1002']
k=[]
for i in t:
    if i < 0:
        i=abs(i)*0
    k.append(i)
E_inn=[]
for o in range(len(fil)):
    P_inn_2 = k[o]*67.2*60
    E_inn.append(P_inn_2)


E_INN = sum(E_inn)   
   


 #virkningsgrad for hele ANLEGET I HELE perioden
VG = Q_Parken/E_INN

"""'Finne total virkingsgraden til solfangerne'"""

T_ut= fil['TE0004']
T_V= fil['TE1201']
T_O=fil['TE1101']


M_V= fil['FE1200']*60/10**3
M_O= fil['FE1100']*60/10**3
C_p= 4183
E_tapt_v=[]
for i in range(len(fil)):
    
    Q= M_V[i]*C_p*(T_V[i]-T_ut[i])
    E_tapt_v.append(Q)
 
Q_tapt_v=sum(E_tapt_v)





E_tapt_O=[]
for i in range(len(fil)):
    
    Q= M_O[i]*C_p*(T_O[i]-T_ut[i])
    E_tapt_O.append(Q)
 
Q_tapt_o=sum(E_tapt_O)


P_fanger= (Q_tapt_v + Q_tapt_o)
VG_SF= P_fanger/E_INN



 









