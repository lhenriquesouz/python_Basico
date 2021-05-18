# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1USKxNy4L5mzsXR8oeVFZSCaMR6Le9gOl
"""

import cv2
from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np

#Selecione uma figura na internet.
!curl -o dead.jpg https://images.unsplash.com/photo-1501432377862-3d0432b87a14?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80

#Através de codificação, importe a figura para dentro do ambiente de trabalho do google colab.
def mostrar(imagem):
    imagem = cv2.cvtColor(imagem,cv2.COLOR_BGR2RGB)
    plt.imshow(imagem)
    plt.show()

dead = cv2.imread("dead.jpg", 1)
mostrar(dead)

#Altere o tamanho da figura (função resize do opencv) para a metade de seu tamanho original e salve um novo arquivo com esta imagem.
width = int(dead.shape[1]/2)
height = int(dead.shape[0]/2)
metade = (width, height)
imgMetade = cv2.resize(dead, metade, interpolation = cv2.INTER_AREA)

mostrar(imgMetade)

#Aumente o tamanho da figura (função resize do opencv) para um tamanho maior (você escolhe) e salve um novo arquivo com esta imagem.
width = int(dead.shape[1]*2)
height = int(dead.shape[0]*2)
dobro = (width, height)
imgDobro = cv2.resize(dead, dobro, interpolation = cv2.INTER_AREA)

mostrar(imgDobro)

#Utilizando a função flip do openCv inverta a imagem horizontalmente e exiba a imagem invertida.
dead_flip_vertical = cv2.flip(dead, 1)
mostrar(dead_flip_vertical)

#Utilizando o conceito de coordenadas, recorte um pedaço da imagem do tamanho que você desejar (que seja visível pelo menos rsrs) e exiba na tela
recortar = dead[2000:3100, 800:1500]
mostrar(recortar)

#Separe os canais da figura (A função split do openCv separa a imagem nos canais R, G e B) e, utilizando a função merge do openCv, crie 3 novas figuras conforme descrito abaixo:
#a)Uma figura contendo apenas os canais verde e vermelho.
(azul, verde, vermelho) = cv2.split(dead)
nulo = np.zeros(dead.shape[:2],dtype="uint8")
Azul = cv2.merge((azul, nulo, vermelho))
Verde = cv2.merge((azul, verde, nulo))
Vermelho = cv2.merge((nulo, verde, vermelho))
mostrar(Azul)
mostrar(Verde)
mostrar(Vermelho)