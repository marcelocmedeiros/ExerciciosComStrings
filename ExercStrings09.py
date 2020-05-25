# Marcelo Campos de Medeiros
# ADS UNIFIP
# Exercicios Com Strings
# https://wiki.python.org.br/ExerciciosComStrings

'''
9- Verificação de CPF. Desenvolva um programa que solicite a digitação de um 
número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou 
inválido através da validação dos dígitos verificadores edos caracteres de formatação.
'''
print('='*30)
print('{:*^30}'.format('  Verificação de CPF '))
print('='*30)
print()

cpf = input("Digite seu CPF(xxx.xxx.xxx-xx): ") #3 7 11

# um laço while para pedir enquato não for digitado corretamente o CPF
# fatie o CPF para ferificar as posições ". e -"
while(cpf[3] !=".") or (cpf[7] !=".") or (cpf[11] !="-"):
    cpf = input("O 'CPF' pricisa estar no formato (xxx.xxx.xxx-xx): ")
else:
    print("O 'CPF' está no formato correto")
