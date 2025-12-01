import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 1. Carregando o Dataset e mostrando partes dos dados

# Primeiro, passamos o caminho do arquivo do Dataset para que ele seja armazenado em uma variável

dados = pd.read_csv('C:\\Users\\gabim\\Downloads\\dataset.txt', sep=',')

# Depois, exibimos as 5 primeiras linhas do Dataset para termos uma noção dos dados que estamos lidando

print("----DATASET----")
print(dados.head())

# 2. Criando a Matriz de Incidência

# Para criar a matriz de incidência, no Python, usamos o pivot_table, o fill_value = 0 garante que os
# valores que não tem logação sejam preenchidos com 0

# A matriz de incidência é uma representação de um grafo onde as linhas representam os vértices (nós) e as colunas representam as arestas
# ou seja, linhas = pessoas, sabores = colunas

matriz_incidencia = dados.pivot_table(index='from', columns='to', values='weight', aggfunc='sum', fill_value=0)

print("\n---- MATRIZ DE INCIDÊNCIA (Pessoas x Sabores) ----")
print(matriz_incidencia)

# 3. Operando matrizes para gerar a Matriz de Similaridade e a Matriz de Coocorrência

# No Python, a função .dot() faz a multiplicação entre as matrizes e a função .T cria a transposta da matriz

similaridade = matriz_incidencia.dot(matriz_incidencia.T)

# Zeramos a diagonal principal

np.fill_diagonal(similaridade.values, 0)

# A Matriz de Similaridade mostra o quão similares são os nós entre si, com base nas conexões que eles compartilham
# ou como no exemplo desse Dataset, quão similares são os usuários com base nos sabores de sorvete que eles gostam

# Pessoa x Pessoa, quem tem gostos parecidos?

print("\n----MATRIZ DE SIMILARIDADE----")
print(similaridade)

# Realizamos o mesmo processo para criar a Matriz de Coocorrência

coocorrencia = matriz_incidencia.T.dot(matriz_incidencia)

# Zeramos a diagonal principal

np.fill_diagonal(coocorrencia.values, 0)

# A Matriz de Coocorrência mostra o quão frequentemente os itens (nós) aparecem juntos nas conexões
# ou como no exemplo desse Dataset, quão frequentemente os sabores de sorvete são escolhidos juntos pelos usuários
print("\n----MATRIZ DE COOCORRÊNCIA----")
print(coocorrencia)

# 4. Visualizando os Grafos com base nas matrizes criadas

plt.figure(figsize=(18, 6))

# Grafo de Incidência

# O grafo de incidência é criado diretamente a partir do DataSet original

# Um grafo de incidência é uma representação visual do grafo onde os nós representam os vértices e as arestas representam as conexões entre eles
grafo_incidencia = nx.from_pandas_edgelist(dados, source='from', target='to', edge_attr='weight', create_using=nx.Graph())

# Plot do Grafo de Incidência

plt.subplot(1, 3, 1)
plt.title("Grafo de Incidência (Dataset Original)")
pos_incidencia = nx.spring_layout(grafo_incidencia)

# Definindo pesos das arestas com base na coluna 'weight' do DataSet

weights_incidencia = [dados['weight'][i] for i in range(len(dados))]
nx.draw(grafo_incidencia, pos_incidencia, with_labels=True, node_color=['lightblue' if n in dados['from'].values else 'orange' for n in grafo_incidencia.nodes()], edge_color='gray', node_size=500, font_size=8)

# Grafo de Similaridade

# o grafo de similaridade é a visualização da Matriz de Similaridade
# onde os nós representam os vértices e as arestas representam o grau de similaridade entre eles

grafo_similaridade = nx.from_pandas_adjacency(similaridade)

# Plot do Grafo de Similaridade
plt.subplot(1, 3, 2)
plt.title("Grafo de Similaridade")
pos_similaridade = nx.spring_layout(grafo_similaridade)

edges_similaridade = grafo_similaridade.edges(data=True)
weights_similaridade = [d['weight'] for (u, v, d) in edges_similaridade]
nx.draw(grafo_similaridade, pos_similaridade, with_labels=True, node_color='lightgreen', width=weights_similaridade)

# Grafo de Coocorrência

# o grafo de coocorrência é a visualização da Matriz de Coocorrência
# onde os nós representam os vértices e as arestas representam o grau de coocorrência entre eles

grafo_coocorrencia = nx.from_pandas_adjacency(coocorrencia)

plt.subplot(1, 3, 3)
plt.title("Grafo de Coocorrência")
pos_coocorrencia = nx.spring_layout(grafo_coocorrencia)
edges_coocorrencia = grafo_coocorrencia.edges(data=True)
weights_coocorrencia = [d['weight'] for (u, v, d) in edges_coocorrencia]
nx.draw(grafo_coocorrencia, pos_coocorrencia, with_labels=True, node_color='salmon', width=weights_coocorrencia)

plt.tight_layout()
plt.show()


# 5. Métricas Topológicas do Grafo de Similaridade

print("\n---- ANÁLISE TOPOLÓGICA (Rede de Similaridade) ----")

num_vertices = grafo_similaridade.number_of_nodes()
num_arestas = grafo_similaridade.number_of_edges()
graus = dict(grafo_similaridade.degree())
grau_medio = sum(graus.values()) / num_vertices if num_vertices > 0 else 0
densidade = nx.density(grafo_similaridade)
pesos_arestas = [d['weight'] for (u, v, d) in grafo_similaridade.edges(data=True)]
conectividade_media = np.mean(pesos_arestas) if pesos_arestas else 0

print(f"Vértices (Pessoas): {num_vertices}")
print(f"Arestas (Conexões): {num_arestas}")
print(f"Grau Médio: {grau_medio:.2f}")
print(f"Densidade da Rede: {densidade:.2f}")
print(f"Conectividade Média (Peso Médio das Arestas): {conectividade_media:.2f}")

# Quem é a pessoa mais "central" (que tem gosto mais comum com todos)?
pessoa_central = max(graus, key=graus.get)
print(f"Pessoa com gostos mais comuns (Maior Grau): {pessoa_central} ({graus[pessoa_central]} conexões)")