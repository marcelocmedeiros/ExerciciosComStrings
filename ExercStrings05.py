# Marcelo Campos de Medeiros
# ADS UNIFIP
# Exercicios Com Strings
# https://wiki.python.org.br/ExerciciosComStrings

'''
5- Nome na vertical em escada invertida. Altere o programa anterior de modo que 
a escada seja invertida.

    FULANO
    FULAN
    FULA
    FUL
    FU
    F
'''
print('='*30)
print('{:*^30}'.format('  Nome na vertical invertida  '))
print('='*30)
print()


# usando for aninhado a outro for

nome = input('Digite seu nome: ')

# len(nome) a segura que podera pegar qualquer nome, pois ele vai colocar o total de letras
for i in range(len(nome), 0, -1):
    for y in range(0, i):
        # end='' para juntar as letras e não sair na vertical a impresão
        print(nome[y], end="")
    print('')

"""# resolvendo com while

nome = input("digite seu nome: ")
print()
i = len(nome)
# com while vai imprimir o nome completo e retirando -1 letra em cada loop até chegar índice 0
while i >= 0:
    print(nome[0:i])
    i = i - 1"""
