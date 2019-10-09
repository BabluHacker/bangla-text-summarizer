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
    output = sorted(set(takingSentPRA).intersection(takingSentRBA))
    output_union = sorted(set(takingSentRBA).union(takingSentPRA))

    '''print(takingSentPRA)
    print(takingSentRBA)
    print('-----------------------------------------------')
    print(output)'''
    out = ""
    out_list = []
    for i in output:
        #print(sent[i],end='\n')
        out_list.append(sent[i])
    out = " ".join(list(set(out_list)))
    #print('\n')

    #print(output_union)
    out_union = ''
    out_union_list = []
    for i in output_union:
        #print(sent[i],end='\n')
        out_union_list.append(sent[i])
    out_union = " ".join(list(set(out_union_list)))
    '''print('\n')
    #graphShow(xyPRA,xyRBA)
    print(" len of out: "+str(len(out)))
    print(out)
    print(" len of out_union: " + str(len(out_union)))
    print(out_union)'''


    ret_text = {}
    ret_text['summarized_text'] = ""
    ret_text['actual_text_size'] = len(text)
    out_size = len(out)
    out_union_size = len(out_union)
    '''if out_union_size >= 700 and out_union_size <= 1000:
        ret_text['summarized_text'] = out_union
        ret_text['summarized_text_size'] = out_union_size
    else:'''
    percentage = float(out_union_size) / float(ret_text['actual_text_size']) # below 30%
    ret_text['percentage'] = percentage
    if out_size == 0 or percentage >= .82:
        ret_text['summarized_text'] = out_union
        ret_text['summarized_text_size'] = out_union_size
        ret_text['type'] = "union"
    else:
        ret_text['summarized_text'] = out
        ret_text['summarized_text_size'] = out_size
        ret_text['type'] = "interasaction"

    return ret_text
