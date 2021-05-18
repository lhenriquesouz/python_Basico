#importar as bibliotecas
import cv2

#lendo a imagem para a variavel imagem
imagem = cv2.imread('figura.png.JPG')

#altura da imagem
print("Altura da iamgem",imagem.shape[0])
#largura da imagem
print("Largura da imagem",imagem.shape[1])

#numero de canais
print("Canais da iamgem",imagem.shape[2])

cv2.imshow("Minha imagem", imagem)
cv2.waitkey(0)


