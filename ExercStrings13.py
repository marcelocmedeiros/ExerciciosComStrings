# Marcelo Campos de Medeiros
# ADS UNIFIP
# Exercicios Com Strings
# https://wiki.python.org.br/ExerciciosComStrings

'''
13- Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha 
que adivinhar uma palavra que será mostrada com as letras embaralhadas. 
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá 
uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. 
Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
'''
print('='*30)
print('{:*^30}'.format(' Jogo da Palavra Embaralhada  '))
print('='*30)
print()

# rodom cria modo aleatório
import random

lista = ["banana", "macaco", "martelo", "jogador", "xarope"]

# random.randint para escolha aleatótia 
palavraEscolhida = lista[random.randint(0, len(lista) - 1)].upper().strip()
# random.sample para embaralhar as letras e .join para juntar as letras
palavraEmbaralhada = ''.join(random.sample(palavraEscolhida,len(palavraEscolhida)))

print(palavraEmbaralhada)

for i in range(1, 7):
    p = input('Digite a palavra pela %dº: ' % i).upper()

    if p == palavraEscolhida:
        print('Você acertou!')
        break
    else:
        if i == 6:
            print('Você perdeu!')
        else:
            print('Você errou!')
   
    