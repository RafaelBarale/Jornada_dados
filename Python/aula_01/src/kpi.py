# Desafio 
"""
O programa deve começar solicitando ao usuário que insira seu nome.
Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
Exemplo de Saída:
Se o usuário digitar "Luciano" como nome, "5000" como salário e "1.5" como bônus, o programa deve imprimir:

Olá Luciano, o seu bônus foi de 8500
Salve esse script python como kpi.py
Faça uma documentação simples de como executar esse programa, utilize o README
Salve no Git e no Github
"""
BONUS = 1000

# 1- O programa deve começar solicitando ao usuário que insira seu nome.
nome = input("Digite o seu nome: ")

# 2- Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
salario_mensal = float(input("Digite o valor mensal: "))

# 3- Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
bonus_usuario = float(input("Digite o percentual para o bonus: "))

# 4- O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
calculo = BONUS + salario_mensal * bonus_usuario

# 5- Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print(f"Olá {nome}! Seu salario total é: {calculo}")
