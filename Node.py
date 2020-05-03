class Node: #criando o nó para a fila e conseguir fazer o expand
    def __init__(self, matriz, custo_heuristica, parent):
        self.matriz = matriz
        self.custo_heuristica = custo_heuristica
        self.parent = parent