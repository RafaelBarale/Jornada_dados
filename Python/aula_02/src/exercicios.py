# Import math Library
import math

# #### Inteiros (`int`)

# # 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# num1 = int(input("Digite um numero: "))
# num2 = int(input("Digite o segundo numero: "))
# print(f"A Soma dos numeros: {num1 + num2}")

# # 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# num1 = int(input("Digite um numero: "))
# resto = num1 % 5
# print(f"Resto da divisão por 5: {resto}")

# # 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# num1 = int(input("Digite um numero: "))
# num2 = int(input("Digite o segundo numero: "))
# print(f"A multiplicação dos numeros: {num1 * num2}")

# # 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# num1 = int(input("Digite um numero: "))
# num2 = int(input("Digite o segundo numero: "))
# print(f"A divisão dos numeros: {num1 // num2}")

# # 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# num1 = int(input("Digite um numero: "))
# print(f"Numero elevado ao quadrado: {num1 ** 2}")

# #### Números de Ponto Flutuante (`float`)

# # 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# num1 = float(input("Digite um numero: "))
# num2 = float(input("Digite o segundo numero: "))
# print(f"A adição dos numeros: {num1 + num2}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# num1 = float(input("Digite um numero: "))
# num2 = float(input("Digite o segundo numero: "))
# print(f"A media dos numeros: {(num1 + num2)/2}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input("Digite um numero: "))
# expoente = float(input("Digite o segundo numero: "))
# print(f"A potencia dos numeros: {base ** expoente}")


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input("Digite a temperatura e celsius: "))
# Fahrenheit = celsius * 1.8 + 32
# print(f"A temperatura em Fahrenheit: {Fahrenheit}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# (A = π r²).
# raio = float(input("Digite o raio: "))
# area = math.pi * raio ** 2
# print(f"A area do circulo: {area}")

# #### Strings (`str`)

# # 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# palavra = input("Digite uma palavra: ")
# print(f"Palavra em maiusculo: {palavra.upper()}")

# # 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = input("Digite uma nome: ")
# print(f"Nome em minusculo: {nome.lower()}")

# # 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input("Digite uma frase: ")
# print(f"frase sem espaços: {frase.strip()}")

# # 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input("Digite uma uma data no formato 'dd/mm/aaaa': ")
# dia, mes, ano = data.split("/")
# print(f"Dia {dia}, mes {mes} e ano{ano}")
# lista = data.split("/")
# print(f"Dia {lista[0]}, mes {lista[1]} e ano{lista[2]}")

# # 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# string1 = input("Digite uma palavra: ")
# string2 = input("Digite a segunda palavra: ")
# print(f"Concatenando as palavras: {string1 + string2}")

# #### Booleanos (`bool`)

# # 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# exp1 = input("Digite True ou False: ")
# exp2 = input("Digite a segunda expressao, True ou False: ")

# bol1 = exp1.lower() in ("yes", "true", "t", "1")
# bol2 = exp2.lower() in ("yes", "true", "t", "1")

# print(f"resultado da operação AND: {bol1 and bol2}")


# # 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# exp1 = input("Digite True ou False: ")
# exp2 = input("Digite a segunda expressao, True ou False: ")

# bol1 = exp1.lower() in ("yes", "true", "t", "1")
# bol2 = exp2.lower() in ("yes", "true", "t", "1")

# print(f"resultado da operação OR: {bol1 or bol2}")


# # 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# exp1 = input("Digite True ou False: ")
# bol1 = exp1.lower() in ("yes", "true", "t", "1")
# print(f"Invertendo o Resultado: {not bol1}")


# # 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# exp1 = float(input("Digite um numero: "))
# exp2 = float(input("Digite segundo numero: "))
# print(f"Os dois numeros são iguais? {exp1 == exp2}")

# # 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# exp1 = float(input("Digite um numero: "))
# exp2 = float(input("Digite segundo numero: "))
# print(f"Os dois numeros são diferentes? {exp1 != exp2}")

# #### try-except e if
# 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, 
# utilizando try-except, garantir que a entrada seja numérica, 
# tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma 
# mensagem de erro se a entrada não for válida
# try:
#   celsius = float(input("Digite a temperatura e celsius: "))
#   Fahrenheit = celsius * 1.8 + 32
#   print(f"A temperatura em Fahrenheit: {Fahrenheit}°F")
# except ValueError:
#   print("Por favor. Digite um número de temperatura válido")


# 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo 
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações).
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.
# palavra = input('Digite uma palavra ou frase ')
# if isinstance(palavra,str):
#   palavra_formatada = palavra.replace(' ','').lower()
#   if palavra_formatada == palavra_formatada[::-1]:
#     print(f'A texto {palavra} é um palíndromo.')
#   else:
#     print(f'A texto {palavra} não é um palíndromo.')
# else:
#   print("Entrada de dados não é string")


# 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas
# e um operador (+, -, *, /) do usuário. Use try-except para lidar com 
# divisões por zero e entradas não numéricas. Utilize if-elif-else para 
# realizar a operação matemática baseada no operador fornecido. Imprima 
# o resultado ou uma mensagem de erro apropriada.
# try:
#   dado1 = input('Digite o primeiro numero: ')
#   operacao = input('Digite a operação: ')
#   dado2 = input ('Digite o segundo numero: ')
  
#   if operacao == '+':
#     resultado = float(dado1) + float(dado2)
#   elif operacao == '-':
#     resultado = float(dado1) - float(dado2)
#   elif operacao == '*':
#     resultado =float( dado1) * float(dado2)
#   elif operacao == '/':
#     try:
#       resultado = float(dado1) / float(dado2)
#     except ZeroDivisionError:
#       print('Divisão por zero não é permitido')
#   else:
#     print('Operador informado de forma errada')
  
#   print(f'Resultado: {resultado}')
# except ValueError:
#   print('Não conseguimos converter para numeros os dados informados.')
# except Exception as e:
#   print(f'Erro gerado {e}')




# 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica e 
# utilize if-elif-else para classificar o número como "positivo", 
# "negativo" ou "zero". Adicionalmente, identifique se o número é 
# "par" ou "ímpar".
# try:
#   dado1 = float(input('Digite o primeiro numero: '))
  
#   if dado1 > 0:
#     resultado = 'Positivo'
#   elif dado1 < 0:
#     resultado = 'Negativo'
#   else:
#     resultado = 'Zero'

#   lPar = (dado1 % 2) == 0

#   print(f'O numero informado: {dado1}, é {resultado}, e {"par" if lPar else 'impar'}')
# except ValueError:
#   print('Não conseguimos converter para numero o dado informado.')
# except Exception as e:
#   print(f'Erro gerado {e}')

# 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números 
# separados por vírgula. O programa deve converter a string de 
# entrada em uma lista de números inteiros. Utilize try-except 
# para tratar a conversão de cada número e validar que cada
# elemento da lista convertida é um inteiro. Se a conversão 
# falhar ou um elemento não for um inteiro, imprima uma mensagem 
# de erro. Se a conversão for bem-sucedida para todos os elementos, 
# imprima a lista de inteiros.

dado1 = input('Digite uma lista de numeros, separados por ",": ')
lista = dado1.split(',')
numeros_int = []
try:
    for num in lista:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
  print('Não conseguimos converter para numero o dado informado.')
except Exception as e:
  print(f'Erro gerado {e}')