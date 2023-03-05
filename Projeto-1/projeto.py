##Importação dos módulos
import matplotlib.pyplot as plt #módulo gráfico
import numpy as np #módulo para trabalhar com arrays

##Definição de funções utilizadas

def curva_equilibrio(alpha,x1):
  return alpha*x1/(1+x1*(alpha - 1))

def intersecao(RR,vB,xD,xB):
  x_intersec = (xD*vB + xB*(RR+1))/(vB + RR + 1)
  y_intersec = (RR/(RR+1))*x_intersec + (1/(RR+1))*xD
  return x_intersec,y_intersec,
  
def retificacao(xR,RR,xD):
  return (RR/(RR+1))*xR + (1/(RR+1))*xD

def esgotamento(xE,vB,xB):
  return ((vB+1)/vB)*xE - (1/vB)*xB

def alimentacao(q,zF,x_intersec,y_intersec):
  if q == 1:
    yA = np.arange(zF,y_intersec+0.0001,0.0001)
    xA = np.full(len(yA),zF)
  else:
    xA = np.arange(x_intersec,zF+0.0001,0.0001)
    yA = (q/(q-1))*xA - zF/(q-1)
  return xA,yA,

def inversa_curva_equilibrio(y,alpha):
  return 1/((alpha/y)+1-alpha)

def retas_horizontais(xD,xB,vB,RR,alpha):
  x_list = [xD]
  y_list = []
  x = xD
  while x >= xB:
    if x > x_intersec:
      y = retificacao(x,RR,xD)
      y_list.append(y)
      x = inversa_curva_equilibrio(y,alpha)
      x_list.append(x)
    else:
      y = esgotamento(x,vB,xB)
      y_list.append(y)
      x = inversa_curva_equilibrio(y,alpha)
      x_list.append(x)
  y_list.append(esgotamento(x,vB,xB))
  return x_list,y_list

##Especificação dos parâmetros do problema

F = 100 #vazão de alimentação [kgmol/h] 
zF = 0.5 #composição da alimentação
RR = 2.56 #razão de refluxo 
alpha = 2 #volatilidade relativa
xB = 0.02
xD = 0.98
x1 = np.arange(0,1.0001,0.0001)
#Balanço para a seção de retificação
D = F*((zF-xB)/(xD-xB))
B = F - D
R = RR*D
V = R + D
L = V*(RR/(RR+1))
#Especificação da alimentação
q = 1
#Balanço para a seção de esgotamento 
L_barra = q*F + L
V_barra = L_barra - B
vB = V_barra/B

##Geração das curvas e retas para a construção do gráfico

#curva de equilíbrio
y1 = curva_equilibrio(alpha,x1)
#cálculo da interseção
x_intersec,y_intersec = intersecao(RR,vB,xD,xB)
#retificacao
xR = np.arange(x_intersec,xD+0.0001,0.0001)
yR = retificacao(xR,RR,xD)
#esgotamento
xE = np.arange(xB,x_intersec+0.0001,0.0001)
yE = esgotamento(xE,vB,xB)
#alimentação
xA,yA = alimentacao(q,zF,x_intersec,y_intersec)
#estagios
x_list,y_list = retas_horizontais(xD,xB,vB,RR,alpha)

#Plot dos estágios teóricos
n_estagios = 0
for i in enumerate(x_list):
  #retas horizontais
  if i[0] < len(x_list) - 2:
    x_axis = np.arange(x_list[i[0]],x_list[i[0]+1]-0.0001,-0.0001)
    y_axis = np.full(len(x_axis),y_list[i[0]])
    plt.plot(x_axis,y_axis,color='gray',linewidth=1)
    #retas verticais
  if i[0] < len(y_list) - 2:
    n_estagios += 1 
    y_axis = np.arange(y_list[i[0]],y_list[i[0]+1]-0.0001,-0.0001)
    x_axis = np.full(len(y_axis),x_list[i[0]+1])
    plt.plot(x_axis,y_axis,color='gray',linewidth=1)

print("N° de pratos teóricos = %i\n" % (n_estagios))

##Construção do gráfico

#curva de equilibrio
plt.plot(x1,y1,linewidth=1,color='black',label='Curva de equilíbrio')
#linha de operação da seção de esgotamento
plt.plot(xE,yE,linewidth=1,color='green', label='LOE')
#linha de operação da seção de retificação
plt.plot(xR,yR,linewidth=1,color='blue',label='LOR')
#linha q (alimentacao)
plt.plot(xA,yA,linewidth=1,color='red',label='Linha-q')
#reta de 45
plt.plot(x1,x1,'--',color = 'black',linewidth=1,label='Diagonal')
#delimitação do topo
aux_xD = np.arange(0,y_list[0]+0.001,0.001)
plt.plot(np.full(len(aux_xD),xD),aux_xD,'--',linewidth=1,color='blue',
         label='Delimitação do topo')
#delimitação da base
aux_xB = np.arange(0,yE[0]+0.001,0.001)
plt.plot(np.full(len(aux_xB),xB),aux_xB,'--',linewidth=1,color='green',
         label='Delimitação da base')
#configuração do gráfico
xmin, xmax, ymin, ymax = 0,1,0,1
plt.axis([xmin, xmax, ymin, ymax])
plt.xlabel('x',fontsize=20)
plt.ylabel('y',fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
#plt.legend(fontsize=14)
plt.show()