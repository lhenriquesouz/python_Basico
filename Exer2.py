A = int(input('Digite o valor para A '))
B = int(input('Digite o valor para B '))
C = int(input('Digite o valor para C '))

print('Numeros', A, B, C)

if  A%2 == 0:
    print('O numero A eh par então: ', B + C)
elif A%2 == 1:
    print('O numero A eh impar então: ', B * C)

