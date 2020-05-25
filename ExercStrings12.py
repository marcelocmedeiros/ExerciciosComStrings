# Marcelo Campos de Medeiros
# ADS UNIFIP
# Exercicios Com Strings
# https://wiki.python.org.br/ExerciciosComStrings

'''
12- Valida e corrige número de telefone. Faça um programa que leia um número de telefone, 
e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. 
O usuário pode informar o número com ou sem o traço separador.

    Valida e corrige número de telefone
    Telefone: 461-0133
    Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
    Telefone corrigido sem formatação: 34610133
    Telefone corrigido com formatação: 3461-0133
'''
print('='*30)
print('{:*^30}'.format('  corrige número de telefone  '))
print('='*30)
print()

numero = int(input('Telefone: '))
print()
# a variável vai receber "3"
novoNumero = ''
if len(str(numero)) < 8:
    diferenca = 8 - len(str(numero))
    novoNumero = '3' * diferenca

# variável vai add "3" no n° informado 
numeroFormatado1 = novoNumero + str(numero)
# variável vai fatiar o número para colocar da form desejada
numeroFormatado = numeroFormatado1[0:4] + '-' + numeroFormatado1[4:]

print('Telefone possui %d dígitos. Vou acrescentar o digito três na frente.' % len(str(numero)))
print('Telefone corrigido sem formatação: %s' % numeroFormatado1)
print('Telefone corrigido com formatação: %s' % numeroFormatado)

'''# outra forma de print formatado
print()
print('Telefone possui {} dígitos. Vou acrescentar o digito três na frente.'.format(len(str(numero))))
print('Telefone corrigido sem formatação: {}'.format(numeroFormatado1))
print('Telefone corrigido com formatação: {}'.format(numeroFormatado))'''