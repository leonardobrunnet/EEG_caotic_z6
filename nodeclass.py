import numpy as np
import matplotlib.pyplot as m
import math as math
import networkx as nx

class node:
    a=-1
    c=-0.9
    beta=0.07
    dt=0.01
    noise=1.0
    bo=5
    bth=2*math.sqrt(a*c)
    tau=1000
    zo=-0.5*bth/a
    def __init__(self, zcomplex, b, ang_freq, neighbors):
        self.z = zcomplex
        self.b = b
        self.w = ang_freq
        self.n = neighbors

    def f(self):
        return (self.a*abs(self.z)**4+self.b*abs(self.z)**2+self.c+self.w*1j)*self.z

    def db(self):
        return (self.bo * (1 - abs(self.z) /self.zo) - self.b) / self.tau
        
    def mov(self):
        soma=0.0
        for i,w in enumerate(self.n):
            soma+=nod[w].z
        soma=self.beta*soma*self.dt 
        self.z+=self.f()*self.dt+self.noise*(np.random.normal(0,.1)+np.random.normal(0,.1)*1.j)*math.sqrt(self.dt)+soma
        self.b+=self.db()*dt
        
#Constructing connection network
N=19
g=nx.Graph()
g.add_node(0)
g.add_node(1)
while not nx.is_connected(g):
    g = nx.erdos_renyi_graph(N,0.5)
    
node_neigh_list=[]
for i in nx.nodes(g):
    list_neigh=[]
    for j in nx.all_neighbors(g, i):
        list_neigh.append(j)
    node_neigh_list.append(list_neigh)


#initialize N nodes
nod=list(node(np.random.normal(0,.1)+np.random.normal(0,.1)*1.j, 2., np.random.normal(2.,0.1), node_neigh_list[i]) for i in range(N))

#Node evolution
t=0
x=[]
d=[]
dt=nod[0].dt
b=[]
k=0
while(t<1000):
    t+=dt
    if(t%100<dt):
        print int(t)
    map(lambda i:i.mov(), nod)
    x.append(t)
    d.append(map(lambda i:abs(i.z), nod))
    b.append(map(lambda i:i.b, nod))

#Graph
m.subplot(2,1,1)
m.plot(x,b)
m.subplot(2,1,2)
m.plot(x,d)
m.show()    


