# Marcelo Campos de Medeiros
# ADS UNIFIP
# Exercicios Com Strings
# https://wiki.python.org.br/ExerciciosComStrings

'''
8- Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é 
idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO 
e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são 
ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde 
os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, 
mostre−a e diga se é um palíndromo ou não.
'''
print('='*30)
print('{:*^30}'.format('  Palíndromo '))
print('='*30)
print()

# usei strip p tirar espaço antes e depois e upper p todas as letras ficarem maiúsculas
palavra = str(input('Digite a palavra: ')).strip().upper()

#usei split para fatiar se for uma frase
frase = palavra.split()

# usei join com espaço vazio para juntar todas as letres se for uma frase
juntar = ''.join(frase)
# depois da string junta inverso recebeu juntar[::-1]
inverso = juntar[::-1]
# com For só tira comentário e comentar o inverso acima
'''# variável "inverso" vai receber o a variável "palavra" invertida pelo FOR
inverso = ''
for letra in range(len(juntar)-1, -1, -1):
    inverso += juntar[letra]'''

# usei if para comparar a variável antes e invertida
if juntar == inverso:
    print('É um palíndromo!')
else:
    print('Não é palíndromo!')

# segundo modo
'''
# usei strip p tirar espaço antes e depois e upper p todas as letras ficarem maiúsculas
palavra = str(input('Digite a palavra: ')).strip().upper()

#usei split para fatiar se for uma frase
frase = palavra.split()

#usei join com espaço vazio para juntar todas as letres se for uma frase
juntar = ''.join(frase)

# usei if para comparrar variável "juntar" e juntar[::-1] que é o inverso
if juntar == juntar[::-1]:
    print('É um palíndromo!')
else:
    print('Não é palíndromo!')
'''