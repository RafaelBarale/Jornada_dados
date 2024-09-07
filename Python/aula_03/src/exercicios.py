### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
# quantidade = 2
# preco = 9
# if quantidade > 0 and preco > 0:
#   print('Dados validos')
# else:
#   print('Dados invalidos')

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# temperatura = 25
# if temperatura < 10:
#   print('Temperatura baixa')
# elif temperatura >= 10 and temperatura <= 25:
#   print('Temperatura media')
# else:
#   print('Temperatura alta')


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
# lista = []
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
# log2= {'timestamp': '2021-06-23 10:00:00', 'level': 'NORMAL', 'message': 'conexão bem sucedida'}
# lista.append(log2)
# lista.append(log)

# for i in lista:
#   if i['level']=='ERROR':
#     print(i['message'])


### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
# try:
#   idade = int(input('Digite sua idade: '))
#   email = input('Informe um email valido: ')

#   if isinstance(email, str):
#     if email.find("@") < 0:
#       print('Email não valido')
#   else:
#     print("Error: Digite um e-mail válido")

#   if not 18 <= idade <= 65:
#     print('Idade invalida')
#   else:
#     print('Dados validos')
# except ValueError:
#   print("Error: Informe um valor válido")


### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
# try:
#   valor = int(input('Informe o valor da transacao: '))
#   hora = 20
#   transacao= {}
#   transacao['valor'] = valor
#   transacao['hora'] = hora

#   if transacao['valor'] > 10000 or not 9 <= transacao['hora'] <= 18:
#     print('Transação suspeita')
#   else:
#     print('Transação validada')
# except ValueError as e:
#   print(f'Error: Dados invalidos {e}')



### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
# text = input('Digite uma frase: ')
# text_formated = text.replace(","," ")
# text_formated = text_formated.replace("."," ").lower()
# dicionario = {}

# lista = text_formated.split()
# for palavra in lista:
#   if palavra in dicionario:
#     dicionario[palavra] += 1
#   else:
#     # dicionario.update( { palavra:1 } )
#     dicionario[palavra] = 1
# print(dicionario)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
# a normalização de dados consiste em colocar todos os dados em uma mesma escala
# o menor numero da lista fica na escala 0 e o maior fica na escala 1
# def normalize_list(lst):
#     return [(i - min(lst)) / (max(lst) - min(lst)) for i in lst]

# numbers = [1, 5, 10, 15, 20]
# normalized_numbers = normalize_list(numbers)
# print(normalized_numbers)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
# lista = []
# lista_chv = ['nome','usuario','senha']
# dic1 = {'nome':'Rafael', 'usuario':'barale', 'senha':'1234'}
# dic2 = {'nome':'Caue', 'usuario':'cibarale'}

# lista.append(dic1)
# lista.append(dic2)
# for i in lista:
#     for chave in lista_chv:
#         if chave not in i:
#             print(f'No dic {i}, falta {chave}')

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
# lista = [5, 10, 13, 18, 24]
# lista_pares = [numero for numero in lista if numero % 2 == 0]
# print(lista_pares)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
# vendas = [
#   {'categoria': 'carros', 'valor':15000},
#   {'categoria': 'moto', 'valor':5000},
#   {'categoria': 'caminhao', 'valor':25000},
#   {'categoria': 'carros', 'valor':500},
# ]
# total_categoria = {}
# for venda in vendas:
#   categoria = venda['categoria']
#   valor = venda['valor']
#   if categoria in total_categoria:
#     total_categoria[categoria] += valor
#   else:
#     total_categoria[categoria] = valor
# print(total_categoria)


### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
# palavra = ''
# while palavra != 'sair':
#   palavra = input('Digite alguma coisa ou "sair", para finalizar ')
#   print(palavra)
# else:
#   print('Finalizado')

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
# numero = 0
# mensagem = 'Digite um numero entre 1 e 5 '
# while numero > 5 or numero < 1:
#   numero = int(input(mensagem))

# print(f'{numero} é valido')

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
# pagina_atual = 1
# paginas_totais = 5  # Simulação, na prática, isso viria da API

# while pagina_atual <= paginas_totais:
#     print(f"Processando página {pagina_atual} de {paginas_totais}")
#     # Aqui iria o código para processar os dados da página
#     pagina_atual += 1

# print("Todas as páginas foram processadas.")

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
# tentativa = 0
# maximo = 10
# while tentativa <= maximo:
#   print(f'Tentativa de conexao {tentativa} de {maximo}')
#   tentativa += 1
# else:
#   print('Falha de conexão')

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
valor_de_parada = 15
lista = [25, 69, 55 ,30 ,15, 22]
i = 0
while i < len(lista):
  if lista[i] == valor_de_parada:
    print('Abortando')
    break

  print(f'Processando numero {lista[i]}')

  i += 1
