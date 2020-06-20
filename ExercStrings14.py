# Marcelo Campos de Medeiros
# ADS UNIFIP
# Exercicios Com Strings
# https://wiki.python.org.br/ExerciciosComStrings

'''
Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.
'''

print('='*30)
print('{:*^30}'.format('  Leet spek generator '))
print('='*30)
print()

#primeiramente deve-se criar o dicióonario para cada letras do alfabeto e sua correspondente
leet = {
    'A': '4',
    'B': '8',
    'C': '<',
    'D': '[)',
    'E': '&',
    'F': 'ph',
    'G': '6',
    'H': '#',
    'I': '1',
    'J': 'j',
    'K': '|<',
    'L': '|_',
    'M': '|\/|',
    'N': '/\/',
    'O': '0',
    'P': '|*',
    'Q': '9',
    'R': 'l2',
    'S': '5',
    'T': '7',
    'U': 'v',
    'V': 'V',
    'W': 'vv',
    'X': '><',
    'Y': '`/',
    'Z': '2'
}

texto = input('Informe um texto: ')
print()

# usando for passar por cada letrar do texto e 
for i in texto.upper():
    # verificar se alfabetico o texto imprime seu correspondete valor
    if i.isalpha():
        print(leet[i], end='')
    else:
        print (' ')
print()
