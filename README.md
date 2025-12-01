# **Análise de Grafos e Matrizes - Preferências de Sorvete 🍦**
Este projeto realiza uma análise de redes complexas baseada em um dataset de preferências de sorvete. O script lê as conexões entre Pessoas e Sabores, gera matrizes relacionais e visualiza os grafos resultantes.

## **O que este código faz?**
- **Leitura de Dados:** Carrega um arquivo `.txt` contendo relações from (Pessoa) → to (Sabor).
- **Matriz de Incidência:** Cria uma matriz relacionando quem escolheu qual sabor.
- **Projeções de Rede:**
  - **Matriz de Similaridade:** Identifica pessoas com gostos parecidos.
  - **Matriz de Coocorrência:** Identifica sabores frequentemente escolhidos juntos.
- **Visualização:** Gera três gráficos (Incidência, Similaridade e Coocorrência).
- **Métricas Topológicas:** Calcula estatísticas como grau médio, conectividade média e densidade.

## **Tecnologias Utilizadas**
- Python 3.x  
- Pandas  
- NumPy  
- NetworkX  
- Matplotlib  

## **Como usar**

**1. Pré-requisitos**  
Certifique-se de ter o Python instalado. Instale as dependências executando:
```
pip install pandas numpy networkx matplotlib
```

**2. Preparar o Dataset**  
Crie um arquivo ```dataset.txt``` no mesmo diretório do script, com o formato:

```
from,to,weight
Laura,Chocolate,1
Daniela,Flocos,1
...
```

**3. Rodar o Script**  
```
python analise_sorvetes.py
```
## Saída esperada  
- **No Terminal:** Matrizes impressas e relatório contendo número de vértices, arestas, grau médio, densidade, etc.

- Na Janela Gráfica: Três grafos:  
 1. Grafo Bipartido (Pessoas → Sabores)

2. Grafo de Similaridade (Pessoa → Pessoa)

3. Grafo de Coocorrência (Sabor → Sabor)