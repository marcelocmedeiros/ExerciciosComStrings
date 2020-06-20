# Marcelo Campos de Medeiros
# ADS UNIFIP
# Exercicios Com Strings
# https://wiki.python.org.br/ExerciciosComStrings

'''
4- Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o 
nome em formato de escada.

    F
    FU
    FUL
    FULA
    FULAN
    FULANO
'''
print('='*30)
print('{:*^30}'.format('  Nome em escada '))
print('='*30)
print()

'''nome = input('Digite seu nome: ').upper()

print('')
# variável somatoria
s = ""
# for com somatória "s" somando cada loop de letra e imprime "s"
for letra in nome:
		s+=letra
		print(s)'''

nome = input("digite seu nome ")
i = 1
while i < len(nome) + 1:
    print(nome[0:i])
    i = i + 1
