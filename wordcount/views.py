from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'home.html')

def wordcount(request):
    wordcount=request.GET['wordcount']
    Totalwords=wordcount.split()
    word_dictionary={}
    for i in Totalwords:
        if i in word_dictionary:
            word_dictionary[i]+=1
        else:
            word_dictionary[i]=1


    return render(request,'count.html',{'words':len(Totalwords),'Text':wordcount,'list':word_dictionary.items()})

def aboutus(request):
    return render(request,'aboutus.html')
