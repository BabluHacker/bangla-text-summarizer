# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 16:40:30 2018

@author: Safi ullah
"""

import networkx as nx
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
    return two
def takingNoun(words):
    Nouns=[]
    poitionOfNouns=[]
    for i in words:
        a=pos().posNoun(i)
        if a:
            poitionOfNouns.append(words.index(a))
            Nouns.append(Stemmer().wordStem(a))
    ret=[]
    ret.append(poitionOfNouns)
    ret.append(Nouns)
    #print(poitionOfNouns,Nouns)
    return ret

#if __name__=="__main__":
def processRBA(text):
    two=makePara(text)
    sent=two[0]
    splitingSent=two[1]
    lenOfPara=len(sent)
    allNouns=[]
    rec=[]
    for i in range(lenOfPara):
        rec=takingNoun(splitingSent[i])
        for j in range(len(rec[0])):
            splitingSent[i][rec[0][j]]=rec[1][j]
            allNouns.append(rec[1][j])
    nouns=[]
    for i in set(allNouns):
        nouns.append(i)
    '''print ("\n\nSplitting sentence")
    print("------------------------------------------------------------")'''
    LengthOfPara=len(sent)
    NoOfNoun=len(nouns)
    '''for i in range(LengthOfPara):
        print(sent[i])
        print(splitingSent[i])'''
    EachSent=[]
    for i in range(LengthOfPara):
        save = []
        for j in nouns:
            if j in splitingSent[i]:
                save.append(j)
        EachSent.append(save)

    '''print ("\n\nDistance calculation")
    print("------------------------------------------------------------")'''
    dis=[]
    g=nx.Graph()
    for i in range(LengthOfPara):
        el=len(EachSent[i])
        if el>1:
            #print el, EachSent[i]
            for j in range(el):
                for k in range(j+1,el):
                    pot = []
                    p = nouns.index(EachSent[i][j])
                    pot.append(p)
                    q = nouns.index(EachSent[i][k])
                    pot.append(q)
                    d = abs(splitingSent[i].index(EachSent[i][j])-splitingSent[i].index(EachSent[i][k]))
                    pot.append(d)
                    dis.append(pot)
                    #print ("dist(",nouns[p],",",nouns[q],")= ",d)
                    # g.add_node(nouns[p])
                    # g.add_node(nouns[q])
                    # g.add_edge(nouns[p],nouns[q])
                    g.add_node(p)
                    g.add_node(q)
                    g.add_edge(p,q)
    '''nx.draw_networkx(g)
    figure = plt.gcf() # get current figure
    figure.set_size_inches(12,8)
    plt.savefig("test.png")
    plt.show()'''

    '''print ("\n\nRelevance calculation")
    print("------------------------------------------------------------")'''
    Rel=[]
    for i in range(NoOfNoun):
        sm=0
        for j in range(len(dis)):
            if dis[j][0]==i or dis[j][1]==i:
                sm+=dis[j][2]
        #keepRel=[]
        #keepRel.append(i)
        #keepRel.append(sum)
        Rel.append(sm)
        #print ("Relavance of",nouns[i],"is :", Rel[i])

    '''print ("\n\nSentence scoring calculation")
    print("------------------------------------------------------------")'''
    scoreOfEachSent=[]
    for i in range(LengthOfPara):
        el = len(EachSent[i])
        total=0
        if el > 1:
            for j in range(el):
                index=nouns.index(EachSent[i][j])
                total+=Rel[index]
            keepSent = []
            keepSent.append(i)
            keepSent.append(total)
            #print keepSent
            scoreOfEachSent.append(keepSent)

    afterSort=[]

    l=len(scoreOfEachSent)
    for i in range(l):
        afterSort.append((scoreOfEachSent[i][0],scoreOfEachSent[i][1]))
        print (scoreOfEachSent[i][0],"no. sentence having scores :",scoreOfEachSent[i][1])

    sentNo=[]
    sentScore=[]
    for i in  range(l):
        sentNo.append(scoreOfEachSent[i][0])
        sentScore.append(scoreOfEachSent[i][1]*339/26213)

    miu=sum(sentScore)/len(sentScore)
    sm=0
    for i in sentScore:
        sm+=(i-miu)**2
    sigma=(sm/len(sentScore))**0.5

    afterSort.sort(key=lambda x:x[1])
    afterSort.reverse()
    takingSent=[]

    if(lenOfPara<30):
        takingWhichSent=math.ceil(lenOfPara/3)
    else:
        takingWhichSent=10
    for i in range(len(afterSort)):
        #print(afterSort[i])
        if i<takingWhichSent:
            takingSent.append(afterSort[i][0])

    '''print("\n\nGetting Summary")

    print("-----------------------------TEST 1--------------------------------")
    print(takingSent)'''
    takingSent.sort()
    '''for i in takingSent:
        #print(sent[i],end='')
        print(sent[i],end='\n')'''
    list_ret = [sent, takingSent]
    return list_ret

class RBA:
    def __init__(self, text):
        self.ret_list = processRBA(text)
    def retNSent(self):
        return self.ret_list[1]

