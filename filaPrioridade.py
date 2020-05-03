import heapq

class filaPrioridade:  # criando a fila de prioridade
    def __init__(self):
        self.fila = []
        self.indice = 0

    def empty_queue(self):
        if len(self.fila) == 0:
            return True
        return False

    def inserirCusto(self, s):
        heapq.heappush(self.fila, (s.custo_heuristica[0], self.indice, s))  # adiciona na fila
        self.indice += 1

    def inserirHeuristica(self, s):
        heapq.heappush(self.fila, (s.custo_heuristica[1], self.indice, s))
        self.indice += 1

    def inserirHeuristicaLivro(self, s):
        heapq.heappush(self.fila, (s.custo_heuristica[2], self.indice, s))
        self.indice += 1

    def inserirCustoHeuristica(self, s):
        heapq.heappush(self.fila, (s.custo_heuristica[0] + s.custo_heuristica[1], self.indice, s))
        self.indice += 1

    def inserirCustoHeuristicaLivro(self, s):
        heapq.heappush(self.fila, (s.custo_heuristica[0] + s.custo_heuristica[2], self.indice, s))
        self.indice += 1

    def remover(self):
        return heapq.heappop(self.fila)[-1]  # apaga o item com prioridade com maior valor