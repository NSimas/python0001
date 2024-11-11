'''
Atividade de Pensar e Responder da Faculdade

primeiro instalei no terminal com o pip tanto o networkx quanto o matplotlib
pip install networkx
pip install matplotlib

'''

import networkx as nx

def criar_grafo_dioxido_de_carbono():

  # Cria um grafo base
  G = nx.Graph()

  # Adiciona os nós (que serão nossos átomos, 3 bolinhas)
  G.add_nodes_from(['C', 'O1', 'O2'])

  # Adiciona as arestas (nossas ligações químicas =}, uma do C pro  o1 e outra do o pro o2)
  G.add_edges_from([('C', 'O1'), ('C', 'O2')])

  return G

# Chamando a função para criar o grafo de água =D
grafo_dioxido_carbono = criar_grafo_dioxido_de_carbono()

# Agora vamos ver nosso grafo bonitão =}
try:
  import matplotlib.pyplot as plt
  nx.draw(grafo_dioxido_carbono, with_labels=True)
  plt.show()
except ImportError:
  print("Para visualizar o grafo, instale a biblioteca matplotlib: pip install matplotlib")