from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request,'home.html')
def count(request):
	fulltext=request.GET['fulltext']
	print(fulltext)
	wordlist=fulltext.split()
	worddict={}
	for word in wordlist:
		if word in worddict:
			#increase
			worddict[word]+=1
		else:
			#add
			worddict[word]=1
	return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddict':worddict.items()})

def aboutus(request):
	return render(request,'aboutus.html')