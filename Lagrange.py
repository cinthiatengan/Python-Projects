# -*- coding: utf-8 -*-
"""cocoDoColli.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tuFIugkfeCiMctNE9XvDFKPiTSkFynHE
"""

import numpy

import numpy as np

import matplotlib.pyplot as plt

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

x_dados = [-2,0,4]
f_dados = [2,-2,1]
x = np.linspace(-2,4,100)

def Lagrange (x_dados, f_dados, x):
  P = np.zeros(len(x))
  for i in range (len(x)):
    L0 = ((x[i]-x_dados[1])*(x[i]-x_dados[2]))/((x_dados[0]-x_dados[1])*(x_dados[0]-x_dados[2]))
    L1 = ((x[i]-x_dados[0])*(x[i]-x_dados[2]))/((x_dados[1]-x_dados[0])*(x_dados[1]-x_dados[2]))
    L2 = ((x[i]-x_dados[0])*(x[i]-x_dados[1]))/((x_dados[2]-x_dados[0])*(x_dados[2]-x_dados[1]))

    P[i]=(f_dados[0]*L0)+(f_dados[1]*L1)+(f_dados[2]*L2)

  return P

P = Lagrange(x_dados, f_dados, x)
P

y=Lagrange(x_dados,f_dados,x)
# COMANDOS PARA PLOTAR O GRÁFICO

# Parâmetro de tamanho do gráfico
tam = 5
# Construção do gráfico
fig = plt.figure(figsize=( tam, tam ))
# Plotando os pontos interpolados com bolinhas
plt.plot( x_dados , f_dados ,'o',markersize=10)
# Plotando a função interpolada -- tracejado
plt.plot(x , y ,'r--', linewidth=1)
# Plotando a interpolação: linha grossa
# plt.plot(x, y , linewidth=2)

