# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 15:16:20 2018

@author: Safi Ullah  
"""

import math
from sentTokenizer import sentTokenizing
from wordConverter import word
from posTagger import pos
from banglaStemmer import Stemmer
import codecs



def makePara(data):
    two=[]
    sent=sentTokenizing().sentTokenize(data)
    two.append(sent)
    two.append(word().sentToWord(sent))
    #print(two[1])
    return two
def takingAdcNoun(fromWhichSent):
    nounsToStemm=[]
    Adjs=[]
    Nouns=[]
    for i in fromWhichSent:
        a=pos().posNoun(i)
        # i mane a single word in a sentence
        if a:
            nounsToStemm.append(a)
        b=pos().posAdj(i)
        if b:
            Adjs.append(b)
    ##print(nounsToStemm)
    ##print(Adjs)
    for i in nounsToStemm:
        Nouns.append(Stemmer().wordStem(i))
    retAdcNouns=Nouns+Adjs
    return retAdcNouns

def createCostMatrix(havingAN):
    lenOfSide=len(havingAN)
    cost=[[0 for i in range(lenOfSide)] for j in range(lenOfSide)]
    ##print(lenOfSide,"--------------------")
    # having lenOfSide is the total sentence
    for i in range(lenOfSide):
        for j in range(i+1,lenOfSide):

            cst=set(havingAN[i]).intersection(havingAN[j])

            cost[i][j]= len(cst)
            cost[j][i]= len(cst)
    ##print(cst,"---------------------------")
    #drawGraph(cost,lenOfSide)
    return cost

def scoreCal(node,degree,Pr):
    sm=0
    N=len(degree)
    d=0.85
    for i in node:
        sm+=Pr[i]/(1.0*degree[i])
    return N/d+(1.0-d)*sm

'''
def drawGraph(getCost,getlenOfSide): #58
    g= nx.Graph()
    getNodes=nx.path_graph(getlenOfSide) 
    g.add_nodes_from(getNodes)
    for i in range(getlenOfSide):
        for j in range(getlenOfSide):
            if i!=j and getCost[i][j]:
                g.add_edge(i,j)
    nx.draw_networkx(g)
    figure = plt.gcf() # get current figure
    figure.set_size_inches(9,6)
    plt.savefig("shafi.png")
    plt.show()'''

#if __name__=="__main__":
def processPRA(text):
    two = makePara(text)
    sent=two[0]
    splitingSent=two[1]

    recAdcNoun=[]
    lenOfPara=len(sent)
    for i in range(lenOfPara):
        recAdcNoun.append(takingAdcNoun(splitingSent[i]))
        ##print(recAdcNoun)
    costMatrix = createCostMatrix(recAdcNoun)
    adcNode=[]
    degree=[]
    for i in range(lenOfPara):
        nodes=[]
        for j in range(lenOfPara):
            if costMatrix[i][j]:
                nodes.append(j)
        adcNode.append(nodes)
        degree.append(sum(costMatrix[i]))
        #print(i,nodes,degree[i])
    Pr=[0.0]*lenOfPara

    it=1000
    while it:
        for i in range(lenOfPara):
            Pr[i]=scoreCal(adcNode[i],degree,Pr)
            ##print(i,'has',Pr[i])
        it-=1

    afterSort=[]
    sm=0
    miu=sum(Pr)/len(Pr)
    for i in range(lenOfPara):
        sm+=(Pr[i]-miu)**2
        afterSort.append((i,Pr[i]))
    sigma=(sm/len(Pr))**0.5

    #print("\n\nGetting sentence number after sorting with their scores")
    #print("----------------------------------------------------------------------")
    afterSort.sort(key=lambda x:x[1])
    afterSort.reverse()
    takingSent=[]
    if(lenOfPara<30):
        takingWhichSent=math.ceil(lenOfPara/3)
    else:

        takingWhichSent=10
    #print(takingWhichSent)
    forcluster=[]
    for i in range(len(afterSort)):
        #print(afterSort[i],"   ",i)
        forcluster.append(afterSort[i][0])
        if i<takingWhichSent:
            #after sort[i][0] mane 1ta sentence er number.
            takingSent.append(afterSort[i][0])

    #print("\n\nGetting Summary")

    #print("-------------------------------------------------------------")

    #with open(filepath, 'w') as textfile:
    takingSent.sort()
    '''for i in takingSent:
        #textfile.write("{}".join(sent[i]))
        #print(sent[i],end='\n')'''
    #textfile.close()
    #print("\n------------------------------------------------------------")
    #print("\n\n Comments on the indivizual Groups described below :")
    ret_sent = [sent, takingSent]
    return ret_sent

class PRA:
    def __init__(self, text):
        self.ret_text = processPRA(text)
    def retNSent(self):
        return self.ret_text[1]

    def retSent(self):
        return self.ret_text[0]
