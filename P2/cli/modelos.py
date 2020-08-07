import networkx as nx
import random

#Funcion para generar una red aleatoria, es decir,modelo de Erdös-Renyi. 
#Le pasamos dos arguemtnos, por una lado el tamaño de la red a generar (N) y por otro la probalidad con la que se enlazan dos nodos (p).
def random_graph(N,p):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    #Declaramos un grafo vacio y lo llenamos con nodos sin enlazar

    for nodo1 in range(N): #cogemos un nodo 
        for nodo2 in range(nodo1 + 1, N): # desde el siguiente nodo a nodo1 buscamos nodos que se puedan enlazar con nodo1
            random_num = random.random() # generamos un numero aleatorio [0.0, 1.0)
            if random_num <= p: # si el numero aleatorio generado es menor o igual que p nodo1 y nodo2 se pueden enlazar
                G.add_edge(nodo1, nodo2) #creamos dicho enlace en el grafo

    return G
