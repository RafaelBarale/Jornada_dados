# 1. Dado uma Lista de números ao quadrado, imprima os numeros ao quadrado
# lista: list = [10, 23, 5, 4]
# for i in lista:
#   print(f"Quadra dos numeros: {i**2}")

# 2. Modificar lista de linguagens, removendo e adicionando elementos
# lista = ['Teste', 'fisica', 'teoria','fisica']
# lista.append('matematica')
# print(lista)
# lista.remove('fisica')
# print(lista)
# lista.pop()
# print(lista)
# lista.pop(-2)
# print(lista)

# 3. Informações de um livro, usando dic, imprima as imformações do livro
# lista: list = ['nome', 'autor', 'ano']
# dicionario: dict = {
#   "nome":"livro1",
#   "autor":"autor1",
#   "ano":"2001"
# }
# print(dicionario.items())
# print(dicionario.values())

# 4. Contar ocorrências de caracteres, passado uma string,faz a contagem de cada caracter
# frase: str = 'Este é um teste de frase e teste de contagem'
# dicionario: dict = {}
# for i in frase:
#   if i in dicionario:
#     # print(f'possui {i}')
#     dicionario[i] += 1
#   else:
#     # print(f'nao possui {i}')
#     dicionario[i] = 1
# print(dicionario)


# 5. Preço total da lista de compras, dado um dicionario de produtos, some o valor total dos produtos
# def total(dicionario:dict):
#   lista_total:list = dicionario.values()
#   total: float = sum(valor for valor in lista_total)
#     # total += i
#   return total

# lista_compras: dict = {
#   "macarrao": 5,
#   "feijao":10,
#   "arroz": 25
# }

# print(total(lista_compras))

# Exercícios intermediários e mais avançados
# 6. Eliminação de Duplicatas = Objetivo: Dada uma lista de emails, remover todos os duplicados.
# lista: list = ['rafael@gmail.com','rafaelbarale@gmail.com','rafael@gmail.com']
# # FUNÇÃO SET ELIMINA TODOS OS DUPLICADOS
# print(set(lista))


# 7. Filtragem de Dados = Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
# def filtragem(numero):
#   return numero >= 18

# idades: list = [15,25,31,7,20,10,55]
# resultado = list(filter(filtragem,idades))
# print(resultado)

# 8. Ordenação Personalizada = Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# def nome(e:list):
#   return e['nome']

# pessoas = [
#   {'nome':'rafael'},
#   {'nome':'caue'},
#   {'nome':'maisa'},
#   {'nome':'alvaro'},
# ]
# pessoas.sort(key=nome)
# print(pessoas)

# 9. Agregação de Dados = Objetivo: Dado um conjunto de números, calcular a média.
# lista: list = [10, 20, 30, 40,50]
# media: float =  sum(lista) / len(lista)
# print(media)

# 10. Divisão de Dados em Grupos = Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
# lista_ini: list = [10, 20, 30, 40, 50, 35, 33, 21, 67, 89]
# lista_par: list = [valor for valor in lista_ini if valor % 2 == 0]
# lista_impar: list =  [valor for valor in lista_ini if valor % 2 != 0]
# # for i in lista_ini:
# #   if i % 2 == 0:
# #     lista_par.append(i)
# #   else:
# #     lista_impar.append(i)
# print(lista_impar)
# print(lista_par)

# Exercícios com Dicionários
# 11. Atualização de Dados = Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
# product_list: list = [
#   { 'id':1, 'nome':'notebook', 'valor': 1000 },
#   { 'id':2, 'nome':'desktop', 'valor': 2000 },
#   { 'id':3, 'nome':'mouse', 'valor': 50  }
# ]
# for product in product_list:
#   if product['nome'] == 'notebook':
#     product['valor'] += product['valor'] * 0.1
  
#   product['valor'] += product['valor'] * 0.2

# print(product_list)



# 12. Fusão de Dicionários = Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
# dicionario1: dict = {'rafael':43}
# dicionario2: dict = {'maisa':44}
# # dicionario_final: dict = {**dicionario1,**dicionario2}
# dicionario_final: dict = {}
# dicionario_final.update(dicionario1)
# dicionario_final.update(dicionario2)

# print(dicionario_final)

# 13. Filtragem de Dados em Dicionário = Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
# product_stock: dict = {
#   'notebook': 2,
#   'mouse': 1,
#   'desktop': 0
# }
# estoque:dict = {produto: qtd for produto, qtd in product_stock.items() if qtd > 0}
# print(estoque)

# 14. Extração de Chaves e Valores = Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
# product_stock: dict = {
#   'notebook': 2,
#   'mouse': 1,
#   'desktop': 0
# }
# lista_chaves: list = list(product_stock.keys())
# lista_valor: list = list(product_stock.values())
# print(lista_chaves)
# print(lista_valor)


# 15. Contagem de Frequência de Itens = Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
# frase: str = 'este é um teste de contagem de caracteres'
# dicionario: dict = {}
# for caracter in frase:
#   if caracter in dicionario:
#     dicionario[caracter] += 1
#   else:
#     dicionario[caracter] = 1
# print(dicionario)



# Exercícios de Funções
# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
# def soma(litsa:list):
#   return sum(lista)

# lista = [2, 3, 4, 5, 6]
# print(soma(lista))


# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
# def isprimo(numero):
#   qtd = (-1 if abs(numero) < 2 else 0)
#   for i in range(1, (numero + 1)): 
#     if numero % i == 0:
#       qtd += 1
#   if qtd != 2:
#     return False
#   else:
#     return True
# print(isprimo(2))


# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
# def revertStr(string: str):
#   return string[::-1]

# print(revertStr('teste'))

# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. 
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.
# def retPares(lista: list, numero: int):
#   return [(i+numero) for i in lista if (i+numero) % 2 == 0 ]
  
# lista = [2, 3, 4, 5]
# print(retPares(lista,3))

# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
# def ret(dicionario: dict):
#   lista_keys = list(dicionario.keys())
#   lista_keys.sort()
#   return lista_keys

# diccio = {
#   "C":1,"A":3
# }

# print(ret(diccio))