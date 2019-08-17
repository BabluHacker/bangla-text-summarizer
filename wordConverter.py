# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 19:31:32 2018

@author: Safi Ullah
"""
class word:
    def sentToWord(self,gettingData):
        cleanData=[]
       # wds=nltk.word_tokenize(gettingData)
        for i in gettingData:
            #print(i)
            cleanSent=''
        
            for j in i:
                if j=='”' or j=='“' or j=='"' or j==',' or j=='‘' or j=='’':
                    continue  
                elif j=='!' or j=='?' or j=='।':  
                    continue  
                elif j=='(' or j=='{' or j=='}' or j=='[' or j==']':
                    cleanSent+=' ' 
                else:
                    if j=='-' or j==':' or j==')': 
                        cleanSent+=' '
                    else:
                        cleanSent+=j
            #print(cleanSent)
            cleanData.append(''.join(cleanSent))
            
        import nltk

        wordsOfEachSent=[]
        for i in cleanData:
            
            wordsOfEachSent.append(nltk.word_tokenize(i))
            
        #print(wordsOfEachSent)
        return wordsOfEachSent
    
#a=word().sentToWord(b)
#print(a)