# Codigo criado para a demonstraçãod e uma busca por largura
# Sua inicialização se dá pela função BuscaLargura (int s)
from collections import defaultdict 

class Graph: 

	def __init__(self): 

		self.graph = defaultdict(list) 

    # Adiciona uma funçãod e borda para a Busca.
	def Borda(self,u,v): 
		self.graph[u].append(v) 

    # imprime o caminho percorrido pela busca
	def BuscaLargura(self, s): 
		
        # Ajusta todos dos vertices como não visitados
		visitado = [False] * (len(self.graph)) 

		queue = [] 

        # Marca o nó como visitado
		queue.append(s) 
		visitado[s] = True

		while queue: 

            # imprime o nodulo visitado
			s = queue.pop(0) 
			print (s, end = " ") 


            # Verifica se o proximo nodulo foi visitado e caso contrário o readiciona a fila
			for i in self.graph[s]: 
				if visitado[i] == False: 
					queue.append(i) 
					visitado[i] = True

# Cria o grafo a ser varrido
g = Graph() 
g.Borda(0, 1) 
g.Borda(0, 2) 
g.Borda(1, 2) 
g.Borda(2, 0) 
g.Borda(2, 3) 
g.Borda(3, 3) 

print ("Busca Cega por Largura"
				" (Começando pelo vertice 2)") 
g.BuscaLargura(2) 