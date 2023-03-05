import numpy as np
from scipy.integrate import odeint 
from pandas import DataFrame 
import matplotlib.pyplot as plt 

#Definindo a função EDO
def edo(y,t):
  Ca, Cb, Cc, Cd, Ce, Cf = y
  dydt = [-k1*Ca*Cb-k2*Ca*(Cc**2), -k1*Ca*Cb-k3*(Cb**2)*(Ce**3), 3*k1*Ca*Cb-k2*Ca*(Cc**2), k1*Ca*Cb, 3*k2*Ca*(Cc**2)-k3*(Cb**2)*(Ce**3), 4*k3*(Cb**2)*(Ce**3)]
  return dydt

#Constante cinética
k1 = 0.10  
k2 = 0.05  
k3 = 0.70  
#condições ininciais
y0 = [2, 1, 0, 0, 0, 0]
t = np.linspace(0, 151, 300)


sol = odeint(edo, y0, t)
Ca = sol [:,0]
Cb = sol [:,1]
Cc = sol [:,2]
Cd = sol [:,3]
Ce = sol [:,4]
Cf = sol [:,5]
df = DataFrame({"Tempo": t, 'Ca': Ca, 'Cb': Cb, 'Cc': Cc, 'Cd': Cd, 'Ce': Ce, 'Cf': Cf})

fig=plt.figure(figsize=(13,8), dpi =80)
plt.plot(t, Ca, 'darkviolet', label='Ca')
plt.plot(t, Cb, 'midnightblue', label='Cb')
plt.plot(t, Cc, 'teal', label='Cc')
plt.plot(t, Cd, 'gold', label='Cd')
plt.plot(t, Ce, 'green', label='Ce')
plt.plot(t, Cf, 'orchid', label='Cf')
plt.legend(loc="best", fontsize = 16)
plt.xlabel('Tempo', fontsize = 16)
plt.ylabel('Concentração das substâncias', fontsize = 16)
plt.title('Concentração em Função do Tempo', fontsize = 16)
plt.show()

'Concentrações finais'
print('Concentrações Finais')
print('Ca = %0.4f' %Ca[-1])
print('Cb = %0.4f' %Cb[-1])
print('Cc = %0.4f' %Cc[-1])
print('Cd = %0.4f' %Cd[-1])
print('Ce = %0.4f' %Ce[-1])
print('Cf = %0.4f' %Cf[-1])