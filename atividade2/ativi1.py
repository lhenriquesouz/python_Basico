import cv2
from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np

imagem = cv2.imread('ft.jpg')

def mostrar(imagem):
    imgNew = cv2.cvtColor(imagem,cv2.COLOR_BGR2RGB)
    plt.imshow(imagem)
    plt.show()

mostrar(imagem)    
