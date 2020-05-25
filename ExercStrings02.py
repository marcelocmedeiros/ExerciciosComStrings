# Marcelo Campos de Medeiros
# ADS UNIFIP
# Exercicios Com Strings
# https://wiki.python.org.br/ExerciciosComStrings

'''
2- Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar 
o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando 
somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode 
digitar letras maiúsculas ou minúsculas.
'''
print('='*30)
print('{:*^30}'.format('  Nome ao contrário  '))
print('='*30)
print()

nome = str(input('Informe seu nome: ')).upper()
# fatia a string copiando ela com :: e mandando imprimir -1 detrás p frente 
print()
print(nome[::-1])
