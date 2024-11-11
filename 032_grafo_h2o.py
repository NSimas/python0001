'''
Atividade de Pensar e Responder da Faculdade

primeiro instalei no terminal com o pip tanto o networkx quanto o matplotlib
pip install networkx
pip install matplotlib

'''

import networkx as nx

def criar_grafo_da_agua():

  # Cria um grafo base
  G = nx.Graph()

  # Adiciona os nós (que serão nossos átomos, 3 bolinhas)
  G.add_nodes_from(['O', 'H1', 'H2'])

  # Adiciona as arestas (nossas ligações químicas =}, uma do o pro  h1 e outra do o pro h2)
  G.add_edges_from([('O', 'H1'), ('O', 'H2')])

  return G

# Chamando a função para criar o grafo de água =D
grafo_agua = criar_grafo_da_agua()

# Agora vamos ver nosso grafo bonitão =}
try:
  import matplotlib.pyplot as plt
  nx.draw(grafo_agua, with_labels=True)
  plt.show()
except ImportError:
  print("Para visualizar o grafo, instale a biblioteca matplotlib: pip install matplotlib")