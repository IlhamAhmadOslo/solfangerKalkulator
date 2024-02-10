# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:41:20 2022

@author: Eier
"""

import pandas as pd
F= pd.read_csv("C:/Users/Eier/Downloads/Timeseries_60.854_8.568_SA_20deg_0deg_2007_2016.csv")
F = F.dropna()

#Mars
F['G(i)'] = F['G(i)'].astype(float)
K=sum(F['G(i)'][1416:2160]) #2007
T=sum(F['G(i)'][10200:10944]) # 2008
H=sum(F['G(i)'][18960:19704]) # 2009
G=sum(F['G(i)'][27720:28464]) # 2010
L=sum(F['G(i)'][36480:37224]) # 2011
D=sum(F['G(i)'][45264:46008]) # 2012
U=sum(F['G(i)'][54024:54768]) # 2013
V=sum(F['G(i)'][62784:63528]) # 2014
S=sum(F['G(i)'][71544:72288]) # 2015
A=sum(F['G(i)'][80328:81072]) # 2016
y=K+T+H+G+L+D+U+S+A+V
R= y/10
energi20072016_1= R*62*0.001

#April
F['G(i)'] = F['G(i)'].astype(float)
K=sum(F['G(i)'][2160:2880]) #2007
T=sum(F['G(i)'][10944:11664]) # 2008
H=sum(F['G(i)'][19704:20424]) # 2009
G=sum(F['G(i)'][28464:29184]) # 2010
L=sum(F['G(i)'][37224:37944]) # 2011
D=sum(F['G(i)'][46008:46728]) # 2012
U=sum(F['G(i)'][54768:55488]) # 2013
V=sum(F['G(i)'][63528:64248]) # 2014
S=sum(F['G(i)'][72288:73008]) # 2015
A=sum(F['G(i)'][81072:81792]) # 2016
y=K+T+H+G+L+D+U+S+A+V
R= y/10
energi20072016_2= R*62*0.001

#mai
F['G(i)'] = F['G(i)'].astype(float)
K=sum(F['G(i)'][2880:3624]) #2007
T=sum(F['G(i)'][11664:12408]) # 2008
H=sum(F['G(i)'][20424:21168]) # 2009
G=sum(F['G(i)'][29184:29928]) # 2010
L=sum(F['G(i)'][37944:38688]) # 2011
D=sum(F['G(i)'][46728:47472]) # 2012
U=sum(F['G(i)'][55488:56232]) # 2013
V=sum(F['G(i)'][64248:64992]) # 2014
S=sum(F['G(i)'][73008:73752]) # 2015
A=sum(F['G(i)'][81792:82536]) # 2016
y=K+T+H+G+L+D+U+S+A+V
R= y/10
energi20072016_3= R*62*0.001


#juni
F['G(i)'] = F['G(i)'].astype(float)
K=sum(F['G(i)'][3624:4344]) #2007
T=sum(F['G(i)'][12408:13128]) # 2008
H=sum(F['G(i)'][21168:21888]) # 2009
G=sum(F['G(i)'][29928:30648]) # 2010
L=sum(F['G(i)'][38688:39408]) # 2011
D=sum(F['G(i)'][47472:48192]) # 2012
U=sum(F['G(i)'][56232:56952]) # 2013
V=sum(F['G(i)'][64992:65712]) # 2014
S=sum(F['G(i)'][73752:74472]) # 2015
A=sum(F['G(i)'][82536:83256]) # 2016
y=K+T+H+G+L+D+U+S+A+V
R= y/10
energi20072016_4= R*62*0.001



#juli
F['G(i)'] = F['G(i)'].astype(float)
K=sum(F['G(i)'][4344:5088]) #2007
T=sum(F['G(i)'][13128:13872]) # 2008
H=sum(F['G(i)'][21888:22632]) # 2009
G=sum(F['G(i)'][30648:31392]) # 2010
L=sum(F['G(i)'][39408:40152]) # 2011
D=sum(F['G(i)'][48192:48936]) # 2012
U=sum(F['G(i)'][56952:57696]) # 2013
V=sum(F['G(i)'][65712:66456]) # 2014
S=sum(F['G(i)'][74472:75216]) # 2015
A=sum(F['G(i)'][83256:84000]) # 2016
y=K+T+H+G+L+D+U+S+A+V
R= y/10
energi20072016_5= R*62*0.001



#august
F['G(i)'] = F['G(i)'].astype(float)
K=sum(F['G(i)'][5088:5832]) #2007
T=sum(F['G(i)'][13872:14616]) # 2008
H=sum(F['G(i)'][22632:23376]) # 2009
G=sum(F['G(i)'][31392:32136]) # 2010
L=sum(F['G(i)'][40152:40896]) # 2011
D=sum(F['G(i)'][48936:49680]) # 2012
U=sum(F['G(i)'][57696:58440]) # 2013
V=sum(F['G(i)'][66456:67200]) # 2014
S=sum(F['G(i)'][75216:75960]) # 2015
A=sum(F['G(i)'][84000:84744]) # 2016
y=K+T+H+G+L+D+U+S+A+V
R= y/10
energi20072016_6= R*62*0.001

#september
F['G(i)'] = F['G(i)'].astype(float)
K=sum(F['G(i)'][5832:6552]) #2007
T=sum(F['G(i)'][14616:15336]) # 2008
H=sum(F['G(i)'][23376:24096]) # 2009
G=sum(F['G(i)'][32136:32856]) # 2010
L=sum(F['G(i)'][40896:41616]) # 2011
D=sum(F['G(i)'][49680:50400]) # 2012
U=sum(F['G(i)'][58440:59160]) # 2013
V=sum(F['G(i)'][67200:67920]) # 2014
S=sum(F['G(i)'][75960:76680]) # 2015
A=sum(F['G(i)'][84744:85464]) # 2016
y=K+T+H+G+L+D+U+S+A+V
R= y/10
energi20072016_7= R*62*0.001

#oktober
F['G(i)'] = F['G(i)'].astype(float)
K=sum(F['G(i)'][6552:7296]) #2007
T=sum(F['G(i)'][15336:16080]) # 2008
H=sum(F['G(i)'][24096:24840]) # 2009
G=sum(F['G(i)'][32856:33600]) # 2010
L=sum(F['G(i)'][41616:42360]) # 2011
D=sum(F['G(i)'][50400:51144]) # 2012
U=sum(F['G(i)'][59160:59904]) # 2013
V=sum(F['G(i)'][67920:68664]) # 2014
S=sum(F['G(i)'][76680:77424]) # 2015
A=sum(F['G(i)'][85464:86208]) # 2016
y=K+T+H+G+L+D+U+S+A+V
R= y/10
energi20072016_8= R*62*0.001

#november
F['G(i)'] = F['G(i)'].astype(float)
K=sum(F['G(i)'][7296:8016]) #2007
T=sum(F['G(i)'][16080:16800]) # 2008
H=sum(F['G(i)'][24840:25560]) # 2009
G=sum(F['G(i)'][33600:34320]) # 2010
L=sum(F['G(i)'][42360:43080]) # 2011
D=sum(F['G(i)'][51144:51864]) # 2012
U=sum(F['G(i)'][59904:60624]) # 2013
V=sum(F['G(i)'][68664:69384]) # 2014
S=sum(F['G(i)'][77424:78144]) # 2015
A=sum(F['G(i)'][86208:86928]) # 2016
y=K+T+H+G+L+D+U+S+A+V
R= y/10
energi20072016_9= R*62*0.001

#elektrisk energi fra 27 pv anlegg og 62m^2

el_1=energi20072016_1*0.202
el_2=energi20072016_2*0.202
el_3=energi20072016_3*0.202
el_4=energi20072016_4*0.202
el_5=energi20072016_5*0.202
el_6=energi20072016_6*0.202
el_7=energi20072016_7*0.202
el_8=energi20072016_8*0.202
el_9=energi20072016_9*0.202


#thermal energi med varme element og vann tank med 0.9 virkningsgrad
th_1=el_1*0.9
th_2=el_2*0.9
th_3=el_3*0.9
th_4=el_4*0.9
th_5=el_5*0.9
th_6=el_6*0.9
th_7=el_7*0.9
th_8=el_8*0.9
th_9=el_9*0.9
thermalenergi= th_1+th_2+th_3+th_4+th_5+th_6+th_7+th_8+th_9




"""
P= pd.read_csv("C:/Users/Eier/Downloads/Timeseries_60.854_8.568_SA_20deg_0deg_2016_2016_bu6.csv")
P = P.dropna()
"""
"""
# April
F['G(i)'] = F['G(i)'].astype(float)
j=sum(F['G(i)'][2184:2904])
energi= j*62*0.001

# Mai
F['G(i)'] = F['G(i)'].astype(float)
l=sum(F['G(i)'][2904:3648])
energi2= l*62*0.001


# juni
F['G(i)'] = F['G(i)'].astype(float)
l2=sum(F['G(i)'][3648:4368])
energi= l2*62*0.001

# juli
F['G(i)'] = F['G(i)'].astype(float)
l=sum(F['G(i)'][4368:5112])
energi2= l*62*0.001


# august
F['G(i)'] = F['G(i)'].astype(float)
l=sum(F['G(i)'][5112:5856])
energi2= l*62*0.001


# september
F['G(i)'] = F['G(i)'].astype(float)
l=sum(F['G(i)'][5856:6600])
energi2= l*62*0.001


# oktober
F['G(i)'] = F['G(i)'].astype(float)
l=sum(F['G(i)'][6600:7344])
energi2= l*62*0.001

# november
F['G(i)'] = F['G(i)'].astype(float)
l=sum(F['G(i)'][7344:8064])
energi2= l*62*0.001

"""



"""
import matplotlib.pyplot as plt

plt.plot(F['G(i)'][1440:2184],F['time'][1440:2184])
"""