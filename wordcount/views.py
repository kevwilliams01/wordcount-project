from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    isare = 'are'
    if len(wordlist) == 1:
        isare = 'is'

    plural = 'words'
    if len(wordlist) == 1:
        plural = 'word'


    wdictionary = {}

    for word in wordlist:
        if word in wdictionary:
            #Increase
            wdictionary[word] += 1
        else:
            #add to the wdictionary
            wdictionary[word] = 1

    sortedwords = sorted(wdictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'chicken':len(wordlist), 'isare': isare, 'plural': plural, 'sortedwords':sortedwords})
