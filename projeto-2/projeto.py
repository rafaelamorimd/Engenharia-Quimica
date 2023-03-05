import numpy as np

def dCa(CAi,CAi_1,k,tau):
  return (CAi_1 - CAi)/tau - k*CAi

k = 0.5
dt = 0.1
t_final = 30
t_p1 = 15
tau = 2
t = np.arange(0,t_final+dt,dt)
CA0,CA01,CA02,CA03 = 1.8, 0.4,0.2,0.1
CA1 = np.zeros(len(t))
CA2 = np.zeros(len(t))
CA3 = np.zeros(len(t))
CA1_p1 = np.zeros((2,len(t[int(t_p1/dt)::])))
CA2_p1 = np.zeros((2,len(t[int(t_p1/dt)::])))
CA3_p1 = np.zeros((2,len(t[int(t_p1/dt)::])))

#sistema sem pertubação

CA1[0] = CA01
CA2[0] = CA02
CA3[0] = CA03
for i in range(len(t)-1):

  CA1[i+1] = CA1[i] + dt*dCa(CA1[i],CA0,k,tau)
  CA2[i+1] = CA2[i] + dt*dCa(CA2[i],CA1[i],k,tau)
  CA3[i+1] = CA3[i] + dt*dCa(CA3[i],CA2[i],k,tau)

#sistema com pertubação

'''
j = variável para especificar o tipo de pertubação
0 - pertubação de grau de +10% na concentração de inicial
1 - pertubação na constate cinética da reação (k = 0.6)
'''

j=1
CA1_p1[j][0] = CA1[int(t_p1/dt)]
CA2_p1[j][0] = CA2[int(t_p1/dt)]
CA3_p1[j][0] = CA3[int(t_p1/dt)]
for i in range(len(t[int(t_p1/dt)::])-1):
  if j == 0:
    CA0_p1 = CA0*1.1
    CA1_p1[j][i+1] = CA1_p1[j][i] + dt*dCa(CA1_p1[j][i],CA0_p1,k,tau)
    CA2_p1[j][i+1] = CA2_p1[j][i] + dt*dCa(CA2_p1[j][i],CA1_p1[j][i],k,tau)
    CA3_p1[j][i+1] = CA3_p1[j][i] + dt*dCa(CA3_p1[j][i],CA2_p1[j][i],k,tau)
  elif j == 1:
    k_p1 = 0.6
    CA1_p1[j][i+1] = CA1_p1[j][i] + dt*dCa(CA1_p1[j][i],CA0,k_p1,tau)
    CA2_p1[j][i+1] = CA2_p1[j][i] + dt*dCa(CA2_p1[j][i],CA1_p1[j][i],k_p1,tau)
    CA3_p1[j][i+1] = CA3_p1[j][i] + dt*dCa(CA3_p1[j][i],CA2_p1[j][i],k_p1,tau)

#Plot do gráfico

import matplotlib.pyplot as plt
plt.plot(t,CA1,color='black',label='$C_{A1}$')
plt.plot(t,CA2,color='blue',label='$C_{A2}$')
plt.plot(t,CA3,color='green',label='$C_{A3}$')
plt.plot(t[int(t_p1/dt)::],CA1_p1[0],
         color = 'red',
         label = 'Pertubação em $C_{A0}$')
plt.plot(t[int(t_p1/dt)::],CA2_p1[0],
         t[int(t_p1/dt)::],CA3_p1[0],
         color='red')
plt.plot(t[int(t_p1/dt)::],CA1_p1[1],
         color='red',linestyle='dashed',
         label = 'Pertubação em k')
plt.plot(t[int(t_p1/dt)::],CA2_p1[1],
         t[int(t_p1/dt)::],CA3_p1[1],
         color='red',linestyle='dashed')
plt.legend(fontsize=14,loc='upper left')
plt.xlabel('Tempo',fontsize=16)
plt.xticks(np.arange(0,35,5),fontsize=16)
plt.yticks(np.arange(0,1.6,0.2),fontsize=16)
plt.ylabel('$C_{A}$',fontsize=16)
plt.rcParams["figure.figsize"]=(14,8)
plt.show()