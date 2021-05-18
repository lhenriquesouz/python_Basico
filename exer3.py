print('Calculando a média')
n1 = int(input('Digite a primeira nota '))
n2 = int(input('Digite a segunda nota '))

media = n1 + n2 / 2

if media<=4:
    print('O aluno foi reprovado')
elif media>4 and media<=6:
    print('O aluno foi para a recuperação')
elif media>=8:
    print('O aluno foi Aprovado')
