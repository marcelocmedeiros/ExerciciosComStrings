# Marcelo Campos de Medeiros
# ADS UNIFIP
# Exercicios Com Strings
# https://wiki.python.org.br/ExerciciosComStrings

'''
9- Verificação de CPF. Desenvolva um programa que solicite a digitação de um 
número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou 
inválido através da validação dos dígitos verificadores e dos caracteres de formatação.
'''
print('='*30)
print('{:*^30}'.format('  Verificação de CPF '))
print('='*30)
print()

# verificação simple apenas do formato
"""cpf = input("Digite seu CPF(xxx.xxx.xxx-xx): ") #3 7 11

# um laço while para pedir enquato não for digitado corretamente o CPF
# fatie o CPF para ferificar as posições ". e -"
while(cpf[3] !=".") or (cpf[7] !=".") or (cpf[11] !="-"):
    cpf = input("O 'CPF' pricisa estar no formato (xxx.xxx.xxx-xx): ")
else:
    print("O 'CPF' está no formato correto")"""

# verificação completa com def
def validaCPF(cpf):
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    if (len(cpf) != 11):
        return False

    # Realiza a multiplicacao dos 9 primeiros numeros
    fator = 10
    soma = 0
    for i in range(0, 9):
        soma += (int(cpf[i]) * fator)
        fator -= 1

    # Divide o somatorio por 11 e pega o resto
    resto = soma % 11

    # Se o resto eh menor que 2, entao o primeiro digito verificador eh 0, senao diminui o resto do valor 11
    if (resto < 2):
        digito1 = 0
    else:
        digito1 = 11 - resto

    # Agora verifica o segundo digito com os 10 primeiros numeros
    fator = 11
    soma = 0
    for i in range(0, 10):
        soma += (int(cpf[i]) * fator)
        fator -= 1

    # Divide o somatorio por 11 e pega o resto
    resto = soma % 11

    # Se o resto eh menor que 2, entao o segundo digito verificador eh 0, senao diminui o resto do valor 11
    if (resto < 2):
        digito2 = 0
    else:
        digito2 = 11 - resto

    if (int(cpf[9]) == digito1) and (int(cpf[10]) == digito2):
        return True
    return False

cpf = input('Informe o CPF: ')
if (validaCPF(cpf)):
    print('CPF valido')
else:
    print('CPF INVALIDO')
