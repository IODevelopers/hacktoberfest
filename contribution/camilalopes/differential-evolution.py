#método EVOLUÇÃO DIFERENCIAL
from scipy.optimize import differential_evolution
import numpy as np
import random as rand
import pylab as gr
from operator import itemgetter
import matplotlib.pyplot as plt

qtInd = 40
dimensao = 2
qtGeracoes = 50
qtExecucoes = 20
F = 0.5 #numero entre [0, 2]
cr = 0.7

def zakharov(x):
    
    n = len(x)
    s1 = 0
    s2 = 0
    for i in range(n):
        s1 += x[i]**2
        s2 += 0.5*(i+1)*x[i]
    
    return s1 + s2**2 + s2**4

def geraPopulacao():
    Pop = np.zeros((qtInd, dimensao), float)
    for i in range(qtInd):
        for j in range(dimensao):
               Pop[i,j] = rand.uniform(-5, 10)

    return Pop

def mutacao(Pop):
    PopMut = np.zeros((qtInd, dimensao), float)
    for i in range(qtInd):
        #sorteio de r
        r1 = rand.randrange(0, qtInd)
        r2 = rand.randrange(0, qtInd)
        r3 = rand.randrange(0, qtInd)
        for j in range(dimensao):
               PopMut[i,j] = Pop[r1, j] + F*(Pop[r3, j] - Pop[r2, j])
    
    return PopMut

def cruzamento(Pop, PopMut):
    U = np.zeros((qtInd, dimensao), float)
    for i in range(qtInd):
        for j in range(dimensao):
            if rand.uniform(0, 1) <= cr:
                U[i, j] = PopMut[i, j]
            else:
                U[i, j] = Pop[i, j]
        indice = rand.randrange(0, dimensao-1)
        U[i, indice] = PopMut[i, indice]
        
    return U
    
def selecao(Pop, U):
    melhores = np.zeros((qtInd, dimensao), float)
    for i in range(qtInd):
        if zakharov(Pop[i]) < zakharov(U[i]):
            melhores[i] = Pop[i]
        else:
            melhores[i] = U[i]
    
    return melhores

def selecao2(Pop, U):
    melhores = []
    for i in range(qtInd):
        melhores.append((Pop[i], zakharov(Pop[i])))
        melhores.append((U[i], zakharov(U[i])))
    
    #ordena minimamente pelo valor da função
    melhores.sort(key=itemgetter(1, 1))
    #retorna apenas os melhores individuos
    resultado = np.zeros((qtInd, dimensao), float)
    for i in range(qtInd):
        resultado[i] = melhores[i][0]
        
    return resultado
    #return melhores[:qtInd]


def main():
    
    r =  np.zeros((qtExecucoes, 3), float)

    for j in range(20):
        Pop = geraPopulacao()
        
        for i in range(qtGeracoes):
            Mut = mutacao(Pop)
            Cruzamento = cruzamento(Pop, Mut)
            Pop = selecao2(Pop, Cruzamento)
        
        resultado = np.zeros((qtInd, 1), float)
        for i in range(qtInd):
            resultado[i] = zakharov(Pop[i])
        
        resultado.sort()
        #print(resultado)
        #print('\nM')
        r[j][0] = resultado[0]
        #print(r[j][0])
        #print('\nP')
        r[j][1] = resultado[qtInd-1]
        #print(r[j][1])
        #print('\nMed')
        r[j][2] = np.mean(resultado)
        #print(r[j][2])
        
    print(r)
    '''print("\nMelhores valores: ")
    print(r[:, 0])
    print("\nMédias: ")
    print(r[:, 2])
    print("\nPiores valores: ")
    print(r[:, 1])'''
    
    print("\nMelhores valores: ")
    gr.plot(r[:, 0])
    gr.show()
    
    plt.hist(r[:, 0], bins=20)
    plt.show()
    
    plt.boxplot(r[:, 0])
    plt.show()
    
    print("\nPiores valores: ")
    gr.plot(r[:, 1])
    gr.show()
    
    plt.hist(r[:, 1], bins=20)
    plt.show()
    
    plt.boxplot(r[:, 1])
    plt.show()

    print("\nMédia: ")
    gr.plot(r[:, 2])
    gr.show()
    
    plt.hist(r[:, 2], bins=20)
    plt.show()
    
    plt.boxplot(r[:, 2])
    plt.show()
    

    
    
     
    
if __name__ == '__main__':
    main()