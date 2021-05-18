print('********* Obtendo o fatorial ***********')
n1 = int(input('Digite um numero '))
fat = 1
i = 2
while i <= n1:
    fat = fat*i
    i = i + 1
    
print('O fatorial de ',n1,' eh ', fat)
