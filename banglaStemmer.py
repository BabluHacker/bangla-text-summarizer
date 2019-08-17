# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 15:09:28 2017

@author: Safi ullah
"""
from xml.dom import minidom

nounLen2=[]
nounLen3=[]
nounLen4=[]
nounLen5=[]
nounLen6=[]
nounLen7=[]
nounLen8=[]
nounLen9=[]
nounLen10=[]
nounLen11=[]
nounLen12=[]
nounLen13=[]
nounLen14=[]
nounLen15=[]
nounLen16=[]
nounLen17=[]
nounLen18=[]
nounLen19=[]
nounLen20=[]
nouns=[]
def gettinNouns():
    xmldoc = minidom.parse('Noun.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nouns.append(s.childNodes[0].nodeValue)
def gettinNounLen2():
    xmldoc = minidom.parse('L1_2.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen2.append(s.childNodes[0].nodeValue)
def gettinNounLen3():
    xmldoc = minidom.parse('L3.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen3.append(s.childNodes[0].nodeValue)
def gettinNounLen4():
    xmldoc = minidom.parse('L4.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen4.append(s.childNodes[0].nodeValue)
def gettinNounLen5():
    xmldoc = minidom.parse('L5.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen5.append(s.childNodes[0].nodeValue)
def gettinNounLen6():
    xmldoc = minidom.parse('L6.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen6.append(s.childNodes[0].nodeValue)
def gettinNounLen7():
    xmldoc = minidom.parse('L7.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen7.append(s.childNodes[0].nodeValue)
def gettinNounLen8():
    xmldoc = minidom.parse('L8.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen8.append(s.childNodes[0].nodeValue)
def gettinNounLen9():
    xmldoc = minidom.parse('L9.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen9.append(s.childNodes[0].nodeValue)
def gettinNounLen10():
    xmldoc = minidom.parse('L10.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen10.append(s.childNodes[0].nodeValue)
def gettinNounLen11():
    xmldoc = minidom.parse('L11.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen11.append(s.childNodes[0].nodeValue)
def gettinNounLen12():
    xmldoc = minidom.parse('L12.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen12.append(s.childNodes[0].nodeValue)
def gettinNounLen13():
    xmldoc = minidom.parse('L13.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen13.append(s.childNodes[0].nodeValue)
def gettinNounLen14():
    xmldoc = minidom.parse('L14.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen14.append(s.childNodes[0].nodeValue)
def gettinNounLen15():
    xmldoc = minidom.parse('L15.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen15.append(s.childNodes[0].nodeValue)
def gettinNounLen16():
    xmldoc = minidom.parse('L16.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen16.append(s.childNodes[0].nodeValue)
def gettinNounLen17():
    xmldoc = minidom.parse('L17.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen17.append(s.childNodes[0].nodeValue)
def gettinNounLen18():
    xmldoc = minidom.parse('L18.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen18.append(s.childNodes[0].nodeValue)
def gettinNounLen19():
    xmldoc = minidom.parse('L19.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen19.append(s.childNodes[0].nodeValue)
def gettinNounLen20():
    xmldoc = minidom.parse('L20.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nounLen20.append(s.childNodes[0].nodeValue)
gettinNouns()
gettinNounLen2()
gettinNounLen3()
gettinNounLen4()
gettinNounLen5()
gettinNounLen6()
gettinNounLen7()
gettinNounLen8()
gettinNounLen9()
gettinNounLen10()
gettinNounLen11()
gettinNounLen12()
gettinNounLen13()
gettinNounLen14()
gettinNounLen15()
gettinNounLen16()
gettinNounLen17()
gettinNounLen18()
gettinNounLen19()
gettinNounLen20()

class Stemmer:
    
    def wordStem(self,s):
        global nouns,nounLen2,nounLen3,nounLen4,nounLen5,nounLen6,nounLen7,nounLen8
        global nounLen10,nounLen11,nounLen12,nounLen13,nounLen14,nounLen15,nounLen16
        global nounLen9,nounLen17,nounLen18,nounLen19,nounLen20
        l=len(s)
        for i in range(l):
            stemmWord=s[:l-i]
            lenOfStemm=len(stemmWord)
            if lenOfStemm==2:
                if stemmWord in nounLen2:
                    return stemmWord
            elif lenOfStemm==3:
                if stemmWord in nounLen3:
                    return stemmWord
            elif lenOfStemm==4:
                if stemmWord in nounLen4:
                    return stemmWord
            elif lenOfStemm==5:
                if stemmWord in nounLen5:
                    return stemmWord
            elif lenOfStemm==6:
                if stemmWord in nounLen6:
                    return stemmWord
            elif lenOfStemm==7:
                if stemmWord in nounLen7:
                    return stemmWord
            elif lenOfStemm==8:
                if stemmWord in nounLen8:
                    return stemmWord
            elif lenOfStemm==9:
                if stemmWord in nounLen9:
                    return stemmWord
            elif lenOfStemm==10:
                if stemmWord in nounLen10:
                    return stemmWord
            elif lenOfStemm==11:
                if stemmWord in nounLen11:
                    return stemmWord
            elif lenOfStemm==12:
                if stemmWord in nounLen12:
                    return stemmWord
            elif lenOfStemm==13:
                if stemmWord in nounLen13:
                    return stemmWord
            elif lenOfStemm==14:
                if stemmWord in nounLen14:
                    return stemmWord
            elif lenOfStemm== 15:
                if stemmWord in nounLen15:
                    return stemmWord
            elif lenOfStemm==16:
                if stemmWord in nounLen16:
                    return stemmWord
            elif lenOfStemm==17:
                if stemmWord in nounLen17:
                    return stemmWord
            elif lenOfStemm==18:
                if stemmWord in nounLen18:
                    return stemmWord
            elif lenOfStemm==19:
                if stemmWord in nounLen19:
                    return stemmWord
            elif lenOfStemm==20:
                if stemmWord in nounLen20:
                    return stemmWord
            else:
                if stemmWord in nouns:
                    return stemmWord
            #print(stemmWord)
        return s
            #print(stemmWord)


#print(Stemmer().wordStem('ছেলের'))