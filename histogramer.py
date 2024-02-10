# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 22:28:41 2022

@author: Eier
"""
import scipy as sp
from scipy.integrate import cumulative_trapezoid
from scipy.integrate import quad
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# areal 90 m^2
F= pd.read_csv("C:/Users/Eier/Downloads/sistesol/sør90.csv")
F = F.dropna()
F['P'] = F['P'].astype(float)

h=[]
for i in F['P']:
    if i  == 0:
        h.append(i)
        

g=[]
for i in F['P']:
    if i  > 0:
        g.append(i)
        
plt.style.use('seaborn-whitegrid')
plt.ylim(1, 16000)
x=plt.hist(g, color = "red", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 90 kvadratmeter for et år")
#y=plt.hist(g)
#inte= cumulative_trapezoid(x[1][0:1000],x[0],initial=1)



# areal 47 m^2
G= pd.read_csv("C:/Users/Eier/Downloads/sistesol/nord47 ekte.csv")
G = G.dropna()
G['P'] = G['P'].astype(float)


q=[]
for i in G['P']:
    if i  == 0:
        q.append(i)
        

t=[]
for i in G['P']:
    if i  > 0:
        t.append(i)
        
plt.style.use('seaborn-whitegrid')
plt.ylim(1, 3000)
x=plt.hist(t, color = "green", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i kW') 
plt.title("Strømproduksjon fra et innstråling areal på 47 kvadratmeter for et år")

# areal 90 + 47
y = G['P'] + F['P']


c=[]
for i in y:
    if i  > 0:
        c.append(i)
        
plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(c, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Strømproduksjon fra et innstråling areal på 137 kvadratmeter for et år')

# Januar
jan1= y[0:744]
r=[]
for i in jan1:
    if i  > 0:
        r.append(i)
        
plt.style.use('seaborn-whitegrid')
plt.ylim(1, 1750)
x=plt.hist(r, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i januar')

#februar

feb= y[744:1440]
f=[]
for i in feb:
    if i  > 0:
        f.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 10000)
x=plt.hist(f, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i februar')

# mars

mar1= y[1440:2184]
m=[]
for i in mar1:
    if i  > 0:
        m.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 14000)
x=plt.hist(m, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i mars')

# april
apr= y[2184:2904]
a=[]
for i in apr:
    if i  > 0:
        a.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 16000)
x=plt.hist(a, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i april')


# mai
mai= y[2904:3648]
ma=[]
for i in mai:
    if i  > 0:
        ma.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(ma, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('Timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i mai')

# juni
jun= y[3648:4368]
ju=[]
for i in jun:
    if i  > 0:
        ju.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(ju, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i juni')

#juli
juli= y[4368:5112]
jul=[]
for i in juli:
    if i  > 0:
        jul.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(jul, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i juli')


#august
aug= y[5112:5856]
au=[]
for i in aug:
    if i  > 0:
        au.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 16000)
x=plt.hist(au, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i august')

# september
sep= y[5856:6576]
o=[]
for i in sep:
    if i  > 0:
        o.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 14000)
x=plt.hist(o, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i september')


#oktober
okt= y[6576:7320]
ok=[]
for i in okt:
    if i  > 0:
        ok.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 10000)
x=plt.hist(ok, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i oktober')



# november
nov= y[7320:8040]
n=[]
for i in nov:
    if i  > 0:
        n.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 6000)
x=plt.hist(n, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i november')

#desember
des= y[8040:8783]
d=[]
for i in des:
    if i  > 0:
        d.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 800)
x=plt.hist(d, color = "brown", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 137 kvadratmeter i desember ')



# hele bygget
S= pd.read_csv("C:/Users/Eier/Downloads/sistesol/s.csv")
S = S.dropna()
S['P'] = S['P'].astype(float)

N= pd.read_csv("C:/Users/Eier/Downloads/no.csv")
N = N.dropna()
N['P'] = N['P'].astype(float)

O= pd.read_csv("C:/Users/Eier/Downloads/sistesol/o.csv")
O = O.dropna()
O['P'] = O['P'].astype(float)

hele = G['P'] + F['P'] + S['P'] + N['P']+ O['P']



#varighetskurve for hele bygget

b=[]
for i in hele:
    if i  > 0:
        b.append(i)
        
plt.style.use('seaborn-whitegrid')
plt.ylim(1, 20000)
x=plt.hist(b, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =1000, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title("Elektrisk produksjon fra et innstråling areal på 156 kvadratmeter for et år")

# Januar
jan= hele[0:744]
r=[]
for i in jan:
    if i  > 0:
        r.append(i)
        
plt.style.use('seaborn-whitegrid')
plt.ylim(1, 1800)
x=plt.hist(r, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i januar')

#februar

feb= hele[744:1440]
f=[]
for i in feb:
    if i  > 0:
        f.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 12000)
x=plt.hist(f, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i februar')

# mars

mar= hele[1440:2184]
m=[]
for i in mar:
    if i  > 0:
        m.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 15000)
x=plt.hist(m, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i mars')

# april
apr= hele[2184:2904]
a=[]
for i in apr:
    if i  > 0:
        a.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 18000)
x=plt.hist(a, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i april')


# mai
mai= hele[2904:3648]
ma=[]
for i in mai:
    if i  > 0:
        ma.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 20000)
x=plt.hist(ma, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i mai')

# juni
jun= hele[3648:4368]
ju=[]
for i in jun:
    if i  > 0:
        ju.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 20000)
x=plt.hist(ju, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i juni')

#juli
juli= hele[4368:5112]
jul=[]
for i in juli:
    if i  > 0:
        jul.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 20000)
x=plt.hist(jul, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i juli')


#august
aug= hele[5112:5856]
au=[]
for i in aug:
    if i  > 0:
        au.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 16000)
x=plt.hist(au, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i august')

# september
sep= hele[5856:6576]
o=[]
for i in sep:
    if i  > 0:
        o.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 15000)
x=plt.hist(o, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i september')


#oktober
okt= hele[6576:7320]
ok=[]
for i in okt:
    if i  > 0:
        ok.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 11000)
x=plt.hist(ok, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i oktober')



# november
nov= hele[7320:8040]
n=[]
for i in nov:
    if i  > 0:
        n.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 6000)
x=plt.hist(n, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i november')

#desember
des= hele[8040:8759]
d=[]
for i in des:
    if i  > 0:
        d.append(i)
        

plt.style.use('seaborn-whitegrid')
plt.ylim(1, 800)
x=plt.hist(d, color = "blue", orientation=u'horizontal', cumulative = -1,  bins =10**3, histtype='step')
plt.xlabel('timer(h)') 
plt.ylabel('Avgitt effekt fra solcellepaneler i W') 
plt.title('Varighetskurve til 156 kvadratmeter i desember')






























