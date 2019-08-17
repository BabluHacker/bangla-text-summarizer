# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 23:30:59 2018

@author: Sofi Ullah
"""
import sys

from RBAfactor import RBA
from PRAfactor import PRA
'''def graphShow(xyPRA,xyRBA):
    xPRA=xyPRA[0]
    yPRA=xyPRA[1]
    xRBA=xyRBA[0]
    yRBA=xyRBA[1]
    plt.plot(yPRA,xPRA,color='green',marker='o',label='PRA')
    plt.plot(yRBA,xRBA,color='red',marker='o',label='RBA')
    plt.xlabel("Score of Sentences")
    plt.ylabel("No of Sentences")
    plt.title("NO vs Score")
    plt.legend()
    plt.show()'''
def start(text):
    sObject = slice(1600)
    stopChar = '।'

    PRAobj=PRA(text=text)
    sent = PRAobj.retSent()
    takingSentPRA = PRAobj.retNSent()
    takingSentRBA=RBA(text=text).retNSent()
    '''xyPRA=PRA().retXY()
    xyRBA=RBA().retXY()'''
    output= sorted(set(takingSentPRA).intersection(takingSentRBA))
    #print('\nOutput Of document')
    output_union = sorted(set(takingSentRBA).union(takingSentPRA))
    '''print(takingSentPRA)
    print(takingSentRBA)
    print('-----------------------------------------------')
    print(output)'''
    out = ""
    for i in output:
        #print(sent[i],end='\n')
        out += sent[i]
        out += ' '
    #print('\n')

    #print(output_union)
    out_union = ''
    for i in output_union:
        #print(sent[i],end='\n')
        out_union += sent[i]
        out_union += ' '
    '''print('\n')
    #graphShow(xyPRA,xyRBA)
    print(" len of out: "+str(len(out)))
    print(out)
    print(" len of out_union: " + str(len(out_union)))
    print(out_union)'''


    ret_text = ""
    if len(out) >= 600 and len(out) <= 900:
        ret_text = out
    else:
        ret_text = out_union
    return ret_text
