# Marcelo Campos de Medeiros
# ADS UNIFIP
# Exercicios Com Strings
# https://wiki.python.org.br/ExerciciosComStrings

'''
11- Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras 
lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes 
antes de ser enforcado.

    Digite uma letra: A
    -> Você errou pela 1ª vez. Tente de novo!

    Digite uma letra: O
    A palavra é: _ _ _ _ O

    Digite uma letra: E
    A palavra é: _ E _ _ O

    Digite uma letra: S
    -> Você errou pela 2ª vez. Tente de novo!

'''
print('='*30)
print('{:*^30}'.format('  Jogo de Forca '))
print('='*30)
print()

# rodom cria modo aleatório
import random

lista = ["banana", "macaco", "martelo", "jogador", "xarope"]

# random.randint para escolha aleatótia
palavraEscolhida = lista[random.randint(0, len(lista) - 1)].upper().strip()

tamanhoPalavra = len(palavraEscolhida)
# cria os trasinho do n° de letras
palavraAdivinhada = ['_'] * tamanhoPalavra

# contador
erros = 0

# join para juntar as letras adivinhadas
print(' '.join(palavraAdivinhada))

while True:
    p = input('Digite uma letra: ').upper().strip()
    cont = 0
    if p in palavraEscolhida:  # letra encontrada
        for pa in palavraEscolhida:
            if pa == p:  # letra encontrada e posição
                palavraAdivinhada[cont] = p
            cont += 1
        if '_' not in ' '.join(palavraAdivinhada):
            print('Você ganhou!')
            print(palavraEscolhida)
            break
    else:
        erros += 1
        if erros >= 6:
            print('Você perdeu a palavra escolhida era %s' % palavraEscolhida)
        else:
            print('Você errou pela %dº vez. Tente novamente.' % erros)
    print(' '.join(palavraAdivinhada))
