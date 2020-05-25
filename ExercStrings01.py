# Marcelo Campos de Medeiros
# ADS UNIFIP
# Exercicios Com Strings
# https://wiki.python.org.br/ExerciciosComStrings

'''
1- Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido 
do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais 
ou diferentes no conteúdo.

    Compara duas strings
    String 1: Brasil Hexa 2006
    String 2: Brasil! Hexa 2006!
    Tamanho de "Brasil Hexa 2006": 16 caracteres
    Tamanho de "Brasil! Hexa 2006!": 18 caracteres
    As duas strings são de tamanhos diferentes.
    As duas strings possuem conteúdo diferente.
'''
print('='*30)
print('{:*^30}'.format('  Comparando strings '))
print('='*30)
print()

frase_1 = input('Escreva: ')
frase_2 = input('Escreva: ')

print()
print('O comprimento da 1° string é {}\nO comprimento da 2° string é {}'.format(len(frase_1), len(frase_2)))

# o if + len() para comparar o tamanho string
if len(frase_1) == len(frase_2):
    print('As duas strings tem o mesmo comprimento!')
else:
    print('As duas strings tem comprimento diferentes!')
# o if + == para comprar se as string são iguais
if frase_1 == frase_2:
    print('As duas strings são iguais!')
else:
    print('As duas strings não são iguais!')
