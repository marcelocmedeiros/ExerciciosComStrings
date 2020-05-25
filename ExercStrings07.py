# Marcelo Campos de Medeiros
# ADS UNIFIP
# Exercicios Com Strings
# https://wiki.python.org.br/ExerciciosComStrings

'''
7- Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário 
(incluindo espaços em branco), conte:

    a- quantos espaços em branco existem na frase.
    b- quantas vezes aparecem as vogais a, e, i, o, u.
'''
print('='*30)
print('{:*^30}'.format('  Conta espaços e vogais '))
print('='*30)
print()


dig = input("Informe uma frase: ")
print()
# usei count() para somar vogais e espaços em branco
s = dig.count("a")+dig.count("e")+dig.count("i")+dig.count("o")+dig.count("u")
print('Há %i espaços na frase.'%(dig.count(" ")))
print('Há %i vogais na frase.'%(s))
print()

print('Há {} espaços na frase.\nHá {} vogais na frase.'.format(dig.count(" "), s))

# usando for
'''
frase = input('Digite a frase: ')
branco = 0
vogais = 0
for f in frase:
    if f == '':
        branco += 1
    if f in 'aeiou':
        vogais += 1

print('Total de espaços em branco: %d' % branco)
print('Total de vogais: %d' % vogais)
'''
