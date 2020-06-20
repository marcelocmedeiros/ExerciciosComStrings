# Marcelo Campos de Medeiros
# ADS UNIFIP
# Exercicios Com Strings
# https://wiki.python.org.br/ExerciciosComStrings

'''
10- Número por extenso. Escreva um programa que solicite ao usuário a digitação 
de um número até 99 e imprima-o na tela por extenso.
'''
print('='*30)
print('{:*^30}'.format('  Número por extenso '))
print('='*30)
print()

#criei listas para converter o número inteiro para seu valor por extenso
# na 1° lista "dezenas" add duas string vazias para representar ínidice 0 e 1
dezenas = [' ', ' ', 'vinte', 'trinta', 'quarenta',
           'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
primeira_dezena = ['dez', 'onze', 'doze', 'treze', 'catorze',
                   'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
unidades = ['zero', 'um', 'dois', 'tres', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove']

numero = int(input('Informe um número entre 0 e 99: '))

# criei um laço while para informar corretamente o valor
while (numero < 0) or (numero > 99):
    numero = int(input('Informe um número entre 0 e 99: '))

else:
    # divisão inteira 
    dezena = numero / 10
    # resto da divisão
    unidade = numero % 10
 
    if (numero >= 20):
        print('%s' % dezenas[int(dezena)], end="")
        if (unidade != 0):
            print(' e %s' % unidades[int(unidade)])
        print('')
    elif (numero >= 10):
        print('%s' % primeira_dezena[int(unidade)])
    else:
        print('%s' % unidades[int(unidade)])
