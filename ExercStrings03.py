# Marcelo Campos de Medeiros
# ADS UNIFIP
# Exercicios Com Strings
# https://wiki.python.org.br/ExerciciosComStrings

'''
3- Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

    F
    U
    L
    A
    N
    O
'''
print('='*30)
print('{:*^30}'.format('  Nome na vertical '))
print('='*30)
print()

nome = input('Escreva seu nome: ').upper()

# usar um for que imprime de índice a índice do nome
print()
for i in nome:
    print(i)
