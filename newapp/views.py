from django.shortcuts import render
from django.http import *
import operator



# Create your views here.
def home(request):
    return render(request,'home.html')

def count(request):
    fulltext =  request.GET['fulltext']
    wordlist = fulltext.split()


    worddict={}

    for word in wordlist:
        if word in worddict:
            #increase
            worddict[word] += 1
        else:
            #add to the dictionary
            worddict[word]= 1

    sortedwords = sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
            
        
    
    
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})

    
def about(request):
    return render(request,'about.html')
