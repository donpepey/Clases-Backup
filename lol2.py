import random

l1=["Palestino","U.Catolica","Cobresal","Colo-Colo","U.Chile"]
l2=["Sao Paulo","Huachipato","Flamengo","Boca Juniors","River Plate"]
l3=["Barcelona","Bayern Munich","Santa Cruz","Inter Milan","PSG"]
l4=["Wolfsburg","Borussia Dortmund","Real Madrid","Atletico Madrid","Real Sociedad"]

g1=[]
g2=[]
g3=[]
g4=[]
g5=[]

listas=[l1,l2,l3,l4]
grupos=[g1,g2,g3,g4,g5]

for g in grupos:
    for l in listas:
        a=random.choice(l)
        g.append(a)
        l.remove(a)
print(g1)
print(g2)
print(g3)
print(g4)
print(g5)