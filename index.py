primeiroDigito = int(input("Digite o primeiro dígito do seu CPF: "))
segundoDigito = int(input("Digite o segundo dígito do seu CPF: "))
terceiroDigito = int(input("Digite o terceiro dígito do seu CPF: "))
quartoDigito = int(input("Digite o quarto dígito do seu CPF: "))
quintoDigito = int(input("Digite o quinto dígito do seu CPF: "))
sextoDigito = int(input("Digite o sexto dígito do seu CPF: "))
setimoDigito = int(input("Digite o sétimo dígito do seu CPF: "))
oitavoDigito = int(input("Digite o oitavo dígito do seu CPF: "))
nonoDigito = int(input("Digite o nono dígito do seu CPF: "))
decimoDigito = int(input("Digite o décimo dígito do seu CPF: "))
decimoPrimeiroDigito = int(
    input("Digite o décimo primeiro dígito do seu CPF: "))

# PRIMEIRO DÍGITO VERIFICADOR

"""
Calculando a soma da multiplicação dos 9 primeiros dígitos, respectivamente,
por 10, 9, 8, ..., 3, 2:
"""

soma1 = (primeiroDigito * 10) + (segundoDigito * 9) + \
    (terceiroDigito * 8) + (quartoDigito * 7) + (quintoDigito * 6) \
    + (sextoDigito * 5) + (setimoDigito * 4) + (oitavoDigito * 3) \
    + (nonoDigito * 2)

# Calculando a divisão inteira e a multiplicação da soma por 11:
valor1 = (soma1 // 11) * 11

# Calculando a subtração de soma e do valor:
resultado1 = soma1 - valor1

if (resultado1 == 1 or resultado1 == 0):
    digito1 = 0
else:
    digito1 = (11 - resultado1)

# SEGUNDO DÍGITO VERIFICADOR:

"""
Calculando a soma da multiplicação dos 9 primeiros dígitos por 11, 10, 9, ... ,
4, 3, respectivamente, e, em seguida, calculamos a soma com (Digito1*2), sendo
que Digito1 é o valor encontrado para o 1º dígito verificador:
"""

soma2 = ((primeiroDigito * 11) + (segundoDigito * 10) +
         (terceiroDigito * 9) + (quartoDigito * 8) + (quintoDigito * 7)
         + (sextoDigito * 6) + (setimoDigito * 5) + (oitavoDigito * 4)
         + (nonoDigito * 3)) + (digito1 * 2)

# Calculando a divisão inteira e a multiplicação da soma por 11:
valor2 = (soma2 // 11) * 11

# Calculando a subtração de soma e do valor:
resultado2 = soma2 - valor2

if (resultado2 == 1 or resultado2 == 0):
    digito2 = 0
else:
    digito2 = (11 - resultado2)

if (digito1 == decimoDigito and digito2 == decimoPrimeiroDigito):
    print("CPF válido!")
else:
    print("CPF inválido!")
