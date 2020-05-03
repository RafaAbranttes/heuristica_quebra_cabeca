from random import randint
import heapq
interacao_solucao = 0
interacao_usuario = 0
queue = []
s10_para_heuristica = 0
s10_custo_heuristica = 0
s10_para_heuristicaLivro  = 0
s10_custo_heuristicaLivro = 0


#condições para o expande
condicao1 = None 
condicao2 = None
condicao3 = None
condicao4 = None


class Node: #criando o nó para a fila e conseguir fazer o expand
    def __init__(self, matriz, custo_heuristica, parent):
        self.matriz = matriz
        self.custo_heuristica = custo_heuristica
        self.parent = parent

class filaPrioridade: #criando a fila de prioridade 
    def __init__(self): 
        self.fila = []
        self.indice = 0

    def empty_queue(self):
        if len(self.fila) == 0:
            return True
        return False

    def inserirCusto(self, s):
        heapq.heappush(self.fila, (s.custo_heuristica[0], self.indice, s)) #adiciona na fila 
        self.indice += 1
    
    def inserirHeuristica(self,s):
        heapq.heappush(self.fila, (s.custo_heuristica[1], self.indice, s))
        self.indice += 1
    
    def inserirHeuristicaLivro(self,s):
        heapq.heappush(self.fila, (s.custo_heuristica[2], self.indice, s))
        self.indice += 1

    def inserirCustoHeuristica(self,s):
        heapq.heappush(self.fila, (s.custo_heuristica[0] + s.custo_heuristica[1], self.indice, s))
        self.indice += 1

    def inserirCustoHeuristicaLivro(self,s):
        heapq.heappush(self.fila, (s.custo_heuristica[0] + s.custo_heuristica[2], self.indice, s))
        self.indice += 1

    def remover(self):
        return heapq.heappop(self.fila)[-1] #apaga o item com prioridade com maior valor
    
def show_fila(s): #mostras tudo que tem na fila de prioridade
    if(s == None):
        return
    for x in range(0,len(s.fila)):
        aux = s.fila[x][2]
        print("-------")
        show_path(aux)
            
    
def copia(s): #realizar uma cópia do nó para não ocorrer erros na troca de valores dos nós
    valor = 0
    linha = []
    aux = []
    aux_custo = [0,0,0]
    condicao_linha = len(s.matriz)
    while(condicao_linha != 0):
        for x in range(0,len(s.matriz)):
            linha.append(valor)
            if(x == len(s.matriz) - 1):
                aux.append(linha)
                linha.clear
                linha = []
                condicao_linha = condicao_linha - 1
    sux = Node(aux,aux_custo,None)
    for x in range(0,len(s.matriz)): #quebra cabeça
        for y in range(0,len(s.matriz[x])):
            sux.matriz[x][y] = s.matriz[x][y] 

    for x in range(0,3): #custo e heuristica
        sux.custo_heuristica[x] = s.custo_heuristica[x]
    return sux

def expande(s): #expande os estados
    list = [] #inicializando a lista
    if(mover_direita(s) == True):
        aux1 = copia(s)
        child1 = movimento_direita(aux1)
        child1.parent = s
        list.append(child1)
    if(mover_esquerda(s) == True):
        aux2 = copia(s)
        child2 = movimento_esquerda(aux2)
        child2.parent = s
        list.append(child2)
    if(mover_cima(s) == True):
        aux3 = copia(s)
        child3 = movimento_cima(aux3)
        child3.parent = s
        list.append(child3)
    if(mover_baixo(s) == True):
        aux4 = copia(s)
        child4 = movimento_baixo(aux4)
        child4.parent = s
        list.append(child4)
    
    return list

def custo(s,valor_heuristica, valor_heuristica_livro):
    s.custo_heuristica[1] = valor_heuristica
    s.custo_heuristica[0] = s.custo_heuristica[0] + 1
    s.custo_heuristica[2] = valor_heuristica_livro
    return s

def mover_direita(s): #analise do valor '0' do quebra cabeça pode realizar o movimento para direita
    for x in range(0,len(s.matriz)):
        for y in range(0,len(s.matriz[x])):
            if(s.matriz[x][y] == 0):
                if(y == 2):
                    return False #retorna falso de o '0' estiver no lado direito
                return True #retorna verdadeiro se o movimento pode acontecer


def mover_esquerda(s): #analise do valor '0' do quebra cabeça poder se movimentar para esquerda
    for x in range(0,len(s.matriz)):
        for y in range(0,len(s.matriz[x])):
            if(s.matriz[x][y] == 0):
                if(y == 0):
                    return False #retorna falso se o '0' estiver no lado esquerdo
                return True #retorna verdadeiro se o movimento pode aonctecer


def mover_cima(s): #anlise do valor '0' do quebra cabeça poder se movimentar para cima 
    for x in range(0,len(s.matriz)):
        for y in range(0,len(s.matriz[x])):
            if(s.matriz[x][y] == 0):
                if(x == 0):
                    return False #retorna falso se o '0' estiver em cima 
                return True #retorna verdadeiro se o movimento pode acontecer


def mover_baixo(s): #analise do valor '0' do quebra cabeça poder se movimentar para baixo
    for x in range(0,len(s.matriz)):
        for y in range(0,len(s.matriz[x])):
            if(s.matriz[x][y] == 0):
                if(x == 2):
                    return False #retorna falso se o '0' estiver em baixo
                return True #retorna 


def movimento_direita(s):
    i = 0
    for x in range(0,len(s.matriz)):
        lista = []
        for y in range(0,len(s.matriz[x])):
            if(s.matriz[x][y] == 0 and i == 0):
                aux = s.matriz[x][y]
                s.matriz[x][y] = s.matriz[x][y + 1]
                s.matriz[x][y + 1] = aux
                i = 1
    valor1 = heuristica(s)
    valor11 = heuristicaLivro(s)
    s1 = custo(s,valor1,valor11)        

    return s1


def movimento_esquerda(s):
    i = 0
    for x in range(0,len(s.matriz)):
        lista = []
        for y in range(0,len(s.matriz[x])):
            if(s.matriz[x][y] == 0 and i == 0):
                aux = s.matriz[x][y]
                s.matriz[x][y] = s.matriz[x][y - 1]
                s.matriz[x][y - 1] = aux
                i = 1
            lista.append(s.matriz[x][y])
    valor2 = heuristica(s)
    valor22 = heuristicaLivro(s)
    s2 = custo(s,valor2,valor22)
    return s2


def movimento_cima(s):
    i = 0
    for x in range (0, len(s.matriz)):
        lista = []
        for y in range (0, len(s.matriz[x])):
            if(s.matriz[x][y] == 0 and i == 0):
                aux = s.matriz[x][y]
                s.matriz[x][y] = s.matriz[x - 1][y]
                s.matriz[x - 1][y] = aux
                i = 1
            lista.append(s.matriz[x][y])
    valor3 = heuristica(s)
    valor33 = heuristicaLivro(s)
    s3 = custo(s,valor3,valor33)
    return s3

def movimento_baixo(s):
    i = 0
    for x in range(0, len(s.matriz)):
        lista = []
        for y in range(0,len(s.matriz[x])):
            if(s.matriz[x][y] == 0 and i == 0):
                aux = s.matriz[x][y]
                s.matriz[x][y] = s.matriz[x+1][y]
                s.matriz[x+1][y] = aux
                i = 1
            lista.append(s.matriz[x][y])
    valor4 = heuristica(s)
    valor44 = heuristicaLivro(s)
    s4 = custo(s,valor4,valor44)
    return s4



def estado_objetivo(tamanho):
    valor = -1
    linha = []
    matriz = []
    condicao_linha = tamanho
    while(condicao_linha != 0):
        for x in range(0,tamanho):
            linha.append(valor+1)
            valor = valor + 1
            if(x == tamanho - 1):
                matriz.append(linha)
                linha.clear
                linha = []
                condicao_linha = condicao_linha - 1

    return Node(matriz,[0,0,0],None)


def goal(iteracao_usuario, interacao_da_solucao):
    if iteracao_usuario == interacao_da_solucao:
        return True
    return False

def goal2(s):
    valor = 0
    for x in range(0,len(s.matriz)):
        for y in range(0,len(s.matriz[x])):
            if (s.matriz[x][y] != valor):
                return False
            valor = valor + 1
    return True


def show_path(s):
    if s == None:
        return
    '''show_path(s.parent)'''
    for x in range(0, len(s.matriz)):
        linha = []
        for y in range(0, len(s.matriz[x])):
            linha.append(s.matriz[x][y])

        print("", linha)
    print("-----------")
    for x in range(0,len(s.custo_heuristica)):
        linha2 = []
        linha2.append(s.custo_heuristica[x])
        print(linha2)
    print("-----------")


def enqueue(s):
    global queue
    queue.append(s)


def dequeue():
    global queue
    ret = queue[0]
    del queue[0]
    return ret


def heuristica(s):
    if s == None:
        return
    matriz_objetivo = estado_objetivo(len(s.matriz))
    tamanho_calculado1 = (len(s.matriz))/2
    calculo1 = 0
    calculo1Dif = 0
    calculo1Fin = 0
    calculo2 = 0
    calculo2Dif = 0
    calculo2Fin = 0
    calculo3 = 0
    calculo3Dif = 0
    calculo3Fin = 0
    calculo4 = 0
    calculo4Dif = 0
    calculo4Fin = 0
    if((len(s.matriz)%2) != 0):
        tamanho_calculado1 += 0.5
        tamanho_calculado = int(tamanho_calculado1)
        for x in range(0,tamanho_calculado): #segundo quadrante
            for y in range(0,tamanho_calculado):
                calculo1 += s.matriz[x][y]
                calculo1Dif += matriz_objetivo.matriz[x][y]
        calculo1Fin = abs(calculo1 - calculo1Dif)

        for x1 in range(0,tamanho_calculado): #primeiro quadrante
            for y1 in range(tamanho_calculado - 1, len(s.matriz)):
                calculo2 += s.matriz[x1][y1]
                calculo2Dif += matriz_objetivo.matriz[x1][y1]
        calculo2Fin = abs(calculo2 - calculo2Dif)

        for x2 in range(tamanho_calculado - 1, len(s.matriz)): #terceiro quadrante
            for y2 in range(0,tamanho_calculado):
                calculo3 += s.matriz[x2][y2]
                calculo3Dif += matriz_objetivo.matriz[x2][y2]
        calculo3Fin = abs(calculo3 - calculo3Dif)

        for x3 in range(tamanho_calculado - 1, len(s.matriz)): #primeiro quadrante
            for y3 in range(tamanho_calculado - 1, len(s.matriz)):
                calculo4 += s.matriz[x3][y3]
                calculo4Dif += matriz_objetivo.matriz[x3][y3]
        calculo4Fin = abs(calculo4 - calculo4Dif)

    
    if((len(s.matriz)%2) == 0):
        tamanho_calculado = int(tamanho_calculado1)
        for x in range(0,tamanho_calculado): #segundo quadrante
            for y in range(0,tamanho_calculado):
                calculo1 += s.matriz[x][y]
                calculo1Dif += matriz_objetivo.matriz[x][y]
        calculo1Fin = abs(calculo1 - calculo1Dif)

        for x1 in range(0,tamanho_calculado): #primeiro quadrante
            for y1 in range(tamanho_calculado - 1, len(s.matriz)):
                calculo2 += s.matriz[x1][y1]
                calculo2Dif += matriz_objetivo.matriz[x1][y1]
        calculo2Fin = abs(calculo2 - calculo2Dif)

        for x2 in range(tamanho_calculado - 1, len(s.matriz)): #terceiro quadrante
            for y2 in range(0,tamanho_calculado):
                calculo3 += s.matriz[x2][y2]
                calculo3Dif += matriz_objetivo.matriz[x2][y2]
        calculo3Fin = abs(calculo3 - calculo3Dif)

        for x3 in range(tamanho_calculado - 1, len(s.matriz)): #primeiro quadrante
            for y3 in range(tamanho_calculado - 1, len(s.matriz)):
                calculo4 += s.matriz[x3][y3]
                calculo4Dif += matriz_objetivo.matriz[x3][y3]
        calculo4Fin = abs(calculo4 - calculo4Dif)
    

    return (calculo1Fin + calculo2Fin + calculo3Fin + calculo4Fin)


def heuristicaLivro(s):
    if s == None:
        return
    matriz_objeitvo = estado_objetivo(len(s.matriz))
    valor = 0
    aux = 0
    for x in range(0,len(s.matriz)):
        for y in range(0,len(s.matriz[x])):
            aux = matriz_objeitvo.matriz[x][y]
            for x1 in range(0,len(s.matriz)):
                for y1 in range(0,len(s.matriz[x1])):
                    if(aux == s.matriz[x1][y1] and aux!= 0):
                        if(x1 != x or y1 != y):
                            valor = valor + abs(x1 - x) + abs(y1 - y)
    
    return valor     

def quebraAleatorio(s1,n_vezes,valor):
    cond = 0
    lista_ale = []
    while(n_vezes != 0):
        if(valor == 0 and  mover_direita(s1) == True):
            '''print ("-----")'''
            s1 = movimento_direita(s1)
            valorHeuristica = heuristica(s1)
            '''show_path(s1)'''
            '''print ("Direita")
            print("",valorHeuristica)'''
            cond = 1
        elif(valor == 0):
            valor = randint(1,3)
            cond = 0
        if(valor == 1 and mover_esquerda(s1) == True):
            '''print("----")'''
            s1 = movimento_esquerda(s1)
            valorHeuristica = heuristica(s1)
            '''show_path(s1)'''
            '''print ("Esquerda")
            print("",valorHeuristica)'''
            cond = 1
        elif(valor == 1):
            valor = randint(0,3)
            while(valor == 1):
                valor = randint(0,3)
            cond = 0
        if(valor == 2 and mover_cima(s1) == True):
            '''print('----')'''
            s1 = movimento_cima(s1)
            valorHeuristica = heuristica(s1)
            '''show_path(s1)'''
            '''print ("Cima")
            print("",valorHeuristica)'''
            cond = 1
        elif(valor == 2):
            valor = randint(0,3)
            while(valor == 2):
                valor = randint(0,3)
            cond = 0
        if(valor == 3 and mover_baixo(s1) == True):
            '''print('----')'''
            s1 = movimento_baixo(s1)
            valorHeuristica = heuristica(s1)
            '''show_path(s1)
            print ("baixo")
            print("",valorHeuristica)'''
            cond = 1
        elif(valor == 3):
            valor = randint(0,3)
            while(valor == 3):
                valor = randint(0,3)
            cond = 0
        if(cond == 1):
            n_vezes = n_vezes - 1
    return s1

def iguais(s1,s2): #s1 estados expandidos #s2 estados visitados
    for x in range(0,len(s2.matriz)):
        for y in range(0,len(s2.matriz[x])):
            if(s2.matriz[x][y] != s1[x][y]):
                return False
    return True


def estadosIguaisVeri(s1,s2): #estados expandidos s1 #estados visitados s2

    for x in range(0,len(s2)):
        aux = s2[x]
        if(iguais(s1,aux)):
            return True    
    return False


def mainCusto():
    custo = 0
    tamanho_tamanho = input("Digite o tamanho do quebra-cabeça. ex: 5 = 5x5 ----->")
    tamanho = int(tamanho_tamanho)
    s11  = estado_objetivo(tamanho) #inicial com o estado objetivo
    valor = randint(0,3) #valor aleatorio de 0 a 3
    # 0 para direita
    # 1 para esquerda
    # 2 para cima
    # 3 para baixo
    n_vezes_n_vezes = input("Digite a quantidade de vezes para embaralhar ----->") #numero de movimentos realizados
    n_vezes = int(n_vezes_n_vezes)

    global s10_para_heuristica #variavel global para utilizar o mesmo estado na heuristica
    global s10_custo_heuristica #variavel global para utilizar o mesmo estado no custo + heurista
    global s10_para_heuristicaLivro 
    global s10_custo_heuristicaLivro

    estados_expandidos = []

    s10 = quebraAleatorio(s11,n_vezes,valor) #recebe o quebra-cabeça aleatorio
    show_path(s10) #mostra o estado aleatorio

    s10_para_heuristica = s10 #adiciona para fazer a busca somente com a heuristica
    s10_custo_heuristica = s10 #adiciona para fazer a busca com custo + heuristica
    s10_para_heuristicaLivro = s10
    s10_custo_heuristicaLivro = s10

    s10.custo_heuristica[0] = 0 #adiciona o custo 0 para iniciar a busca
    fila = filaPrioridade() #inicia a lista de prioridade
    listaVisi = [] #inicialização da lista para os estados visitados
    fila.inserirCusto(s10) #inserir o primeiro estado na fila de prioridade
    print("------------CUSTO--------------------")

    while not fila.empty_queue(): #olha se a fila esta vazia
        s30 = fila.remover() #remove o estado com maior prioridade
        estados_expandidos.append(s30)
        listaVisi.append(s30) #adiciona o estado visitado na lista
        if goal2(s30): #analisa se chegou no estado objetivo
            show_path(s30) #mostra o caminho realizado
            print ("----Estados Expandidos----")
            print ("",len(estados_expandidos))
            return True

        children = expande(s30) #função expande 

        for child in children: 
            
            if(not estadosIguaisVeri(child.matriz,listaVisi)): #analise de estados repetidos
                fila.inserirCusto(child) #caso não exista estado repetido ele adiciona na fila de prioridade

    return False


def mainHeuristica():
    print("------------HEURISTICA--------------------")

    s10_para_heuristica.custo_heuristica[0] = 0 #custo 0 para a heuristica
    filaHeuristica = filaPrioridade() #inicia a fila para a heuristica
    listaVisiHeuristica = [] #inicia a lista para heuristica
    estados_expandidos_heuristica = []
    filaHeuristica.inserirHeuristica(s10_para_heuristica) #adiciona o estado na fila de prioridade

    while not filaHeuristica.empty_queue(): #caso a fila não esteja vazia

        s30Heuristica = filaHeuristica.remover() #remove o estado com maior prioridade
        estados_expandidos_heuristica.append(s30Heuristica)
        listaVisiHeuristica.append(s30Heuristica) #adiciona o estado visitado na lista

        if goal2(s30Heuristica): #analida o estado objetivo
            show_path(s30Heuristica) #mostra o caminho
            print ("----Estados Expandidos----")
            print ("",len(estados_expandidos_heuristica))
            return True

        childrenHeuristica = expande(s30Heuristica) #função expande

        for childHeuristica in childrenHeuristica: 
            
            if(not estadosIguaisVeri(childHeuristica.matriz,listaVisiHeuristica)): #para estados repetidos
                filaHeuristica.inserirHeuristica(childHeuristica) #adiciona na fila estados diferentes

    return False

def mainHeuristicaLivro():
    print("------------HEURISTICA(LIVRO)--------------------")

    s10_para_heuristicaLivro.custo_heuristica[0] = 0 #custo 0 para a heuristica
    filaHeuristicaLivro = filaPrioridade() #inicia a fila para a heuristica
    listaVisiHeuristicaLivro = [] #inicia a lista para heuristica
    estados_expandidos_heuristicaLivro = []
    filaHeuristicaLivro.inserirHeuristicaLivro(s10_para_heuristicaLivro) #adiciona o estado na fila de prioridade

    while not filaHeuristicaLivro.empty_queue(): #caso a fila não esteja vazia

        s30HeuristicaLivro = filaHeuristicaLivro.remover() #remove o estado com maior prioridade
        estados_expandidos_heuristicaLivro.append(s30HeuristicaLivro)
        listaVisiHeuristicaLivro.append(s30HeuristicaLivro) #adiciona o estado visitado na lista

        if goal2(s30HeuristicaLivro): #analida o estado objetivo
            show_path(s30HeuristicaLivro) #mostra o caminho
            print ("----Estados Expandidos----")
            print ("",len(estados_expandidos_heuristicaLivro))
            return True

        childrenHeuristicaLivro = expande(s30HeuristicaLivro) #função expande

        for childHeuristicaLivro in childrenHeuristicaLivro: 
            
            if(not estadosIguaisVeri(childHeuristicaLivro.matriz,listaVisiHeuristicaLivro)): #para estados repetidos
                filaHeuristicaLivro.inserirHeuristicaLivro(childHeuristicaLivro) #adiciona na fila estados diferentes

    return False

def mainCustoHeuristica():

    print("------------CUSTO + HEURISTICA--------------------")
    s10_custo_heuristica.custo_heuristica[0] = 0 #adiciona o custo 0 para iniciar a busca
    fila_custo_heuristica = filaPrioridade() #inicia a lista de prioridade
    listaVisi_custo_heuristica = [] #inicialização da lista para os estados visitados
    fila_custo_heuristica.inserirCustoHeuristica(s10_custo_heuristica) #inserir o primeiro estado na fila de prioridade
    estados_expandidos_custo_heuristica = []
    while not fila_custo_heuristica.empty_queue(): #olha se a fila esta vazia
        s30_custo_heuristica = fila_custo_heuristica.remover() #remove o estado com maior prioridade
        listaVisi_custo_heuristica.append(s30_custo_heuristica) #adiciona o estado visitado na lista
        estados_expandidos_custo_heuristica.append(s30_custo_heuristica)
        if goal2(s30_custo_heuristica): #analisa se chegou no estado objetivo
            show_path(s30_custo_heuristica) #mostra o caminho realizado
            print ("----Estados Expandidos----")
            print ("",len(estados_expandidos_custo_heuristica))
            return True

        children_custo_heuristica = expande(s30_custo_heuristica) #função expande 

        for child_custo_heuristica in children_custo_heuristica: 
            
            if(not estadosIguaisVeri(child_custo_heuristica.matriz,listaVisi_custo_heuristica)): #analise de estados repetidos
                fila_custo_heuristica.inserirCustoHeuristica(child_custo_heuristica) #caso não exista estado repetido ele adiciona na fila de prioridade

    return False


def mainCustoHeuristicaLivro():
    
    print("------------CUSTO + HEURISTICA(livro)--------------------")
    s10_custo_heuristicaLivro.custo_heuristica[0] = 0 #adiciona o custo 0 para iniciar a busca
    fila_custo_heuristicaLivro = filaPrioridade() #inicia a lista de prioridade
    listaVisi_custo_heuristicaLivro = [] #inicialização da lista para os estados visitados
    fila_custo_heuristicaLivro.inserirCustoHeuristicaLivro(s10_custo_heuristicaLivro) #inserir o primeiro estado na fila de prioridade
    estados_expandidos_custo_heuristicaLivro = []
    while not fila_custo_heuristicaLivro.empty_queue(): #olha se a fila esta vazia
        s30_custo_heuristicaLivro = fila_custo_heuristicaLivro.remover() #remove o estado com maior prioridade
        listaVisi_custo_heuristicaLivro.append(s30_custo_heuristicaLivro) #adiciona o estado visitado na lista
        estados_expandidos_custo_heuristicaLivro.append(s30_custo_heuristicaLivro)
        if goal2(s30_custo_heuristicaLivro): #analisa se chegou no estado objetivo
            show_path(s30_custo_heuristicaLivro) #mostra o caminho realizado
            print ("----Estados Expandidos----")
            print ("",len(estados_expandidos_custo_heuristicaLivro))
            return True

        children_custo_heuristicaLivro = expande(s30_custo_heuristicaLivro) #função expande 

        for child_custo_heuristicaLivro in children_custo_heuristicaLivro: 
            
            if(not estadosIguaisVeri(child_custo_heuristicaLivro.matriz,listaVisi_custo_heuristicaLivro)): #analise de estados repetidos
                fila_custo_heuristicaLivro.inserirCustoHeuristicaLivro(child_custo_heuristicaLivro) #caso não exista estado repetido ele adiciona na fila de prioridade

    return False


mainCusto()
mainHeuristica()
mainHeuristicaLivro()
mainCustoHeuristica()
mainCustoHeuristica()