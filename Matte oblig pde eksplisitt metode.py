#PDE numerisk løsning for varmelikningen i 3 dimensjoner med eksplisitt metode
import numpy as np
import matplotlib.pyplot as plt

h=0.025
k=0.025
x=np.arange(0,1+h, h)
t=np.arange(0,0.1+k, h)
boundaryConditions= [0,0]
initialConditions=np.sin(np.pi*x)


n=len(x)
m=len(t)
T=np.zeros((n,m))
T[0,:]=boundaryConditions[0]
T[-1, :]=boundaryConditions[1]
T[:,0]= initialConditions
T.round(3)
factor=k/h**2
for j in range(1,m):
    for i in range(1,n-1):
        T[i,j]=factor*T[i-1,j-1]+(1-2*factor)*T[i,j-1]+ factor*T[i+1,j-1]
T.round(3)



R=np.linspace(1,0,m)
B=np.linspace(0,1,m)
G=0

for j in range(m):
    plt.plot(x, T[:,j], color=[R[j],G,B[j]])

plt.legend(t)
plt.xlabel('avstand [m]')
plt.ylabel('Temperatur [Celsius]')