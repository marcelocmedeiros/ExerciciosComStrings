# Marcelo Campos de Medeiros
# ADS UNIFIP
# Exercicios Com Strings
# https://wiki.python.org.br/ExerciciosComStrings

'''
6- Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do 
usuário e imprima a data com o nome do mês por extenso.

    Data de Nascimento: 29/10/1973
    Você nasceu em  29 de Outubro de 1973.
'''
print('='*30)
print('{:*^30}'.format('  Data por extenso '))
print('='*30)
print()

data = input('Data de Nascimento:(dd/mm/aaaa): ')
print()
# criei uma lista dos meses do ano para depois de fatiar a string converter em int e sub -1 p pegar 
# o índice correspondente a lista dos meses do ano
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Em dia e ano fatio a string e converto em inteiro. 
dia = int(data[0:2])
mes = meses[int(data[3:5]) - 1]
ano = int(data[6:])

print('Você nasceu em %d de %s de %d' % (dia, mes, ano))
print('Você nasceu em {} de {} de {}'.format(dia, mes, ano))
print(f'Você nasceu em {dia} de {mes} de {ano}')
