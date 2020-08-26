# Programa criado para a disciplina Inteligencia Artificial
# Demonstra um codigo de uma Busca Heuristica (A*)

# Chama a biblioteca python-constraint
from constraint import *


# Cria e adiciona as variaveis ao "problema"
problem = Problem ()

# Limita até onde os numeros podem ser escolhidos, de 0-9
problem.addVariable('a', range(10))
problem.addVariable('b', range(10))

# Adiciona a regra do problema que vai procurar pares de numeros em que b seja o dobro de a, ainda limitado pelo range acima. 
problem.addConstraint(lambda a, b: a * 2 == b)

# Mostra as soluções do problema
solutions = problem.getSolutions()

print (solutions)