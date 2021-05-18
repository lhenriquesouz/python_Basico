print('Digite a sequencia de 5 numeros: ')
n1 = int(input('Primeiro número '))
n2 = int(input('Segundo número '))
n3 = int(input('terceiro número ')) 
n4 = int(input('Quarto número '))
n5 = int(input('Quinto número '))

N=[n1,n2,n3,n4,n5]
print('Ordem original:',N)
print('Ordem crescente:',sorted(N))
print('Ordem decrescente:',sorted(N,reverse = True))
