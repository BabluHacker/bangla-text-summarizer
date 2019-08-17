# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 15:20:23 2018

@author: Safi ullah
"""
'''
import codecs
with codecs.open("S.txt",'r',encoding="utf-8") as myfile:
    text= myfile.read()'''
class sentTokenizing:
    def sentTokenize(self,gettingText):
        dataToReSize=[]
        data=[]
        cleanText=''
        for i in gettingText:
            if i=='।' or i=='!' or i=='?':
                cleanText+=i
                dataToReSize.append(''.join(cleanText))
                cleanText=''
            else:
                if i=='\n' or i=='\r' or i=='”' or i=='“' or i=='"':
                    continue
                else:
                    cleanText+=i
        #print (dataToReSize)
        for i in dataToReSize:
            withoutAheadSpace=''
            flag=1
            for j in i:
                if j==' ' and flag: # sentence er surote soto space ase sobgolu remove korar jonno
                    continue
                else:
                    flag=0
                    withoutAheadSpace+=j
            data.append(''.join(withoutAheadSpace))
        #print(data)
                
        return data
 
#a=sentTokenizing().sentTokenize(text)
#print(a)