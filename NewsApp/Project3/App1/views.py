from django.shortcuts import render

# Create your views here.
# importing the required api  
from django.shortcuts import render  
from newsapi import NewsApiClient  
# Creating our views here.  
def indexin(request):  
    newsapii = NewsApiClient(api_key ='040e567eb52f4b3b91e25a194cfe7361')  
    top = newsapii.get_top_headlines(sources ='techcrunch')  
    l = top['articles']  
    descr =[]  
    news =[]  
    imgi =[]  
    for i in range(len(l)):  
        fj = l[i]  
        news.append(fj['title'])  
        descr.append(fj['description'])  
        imgi.append(fj['urlToImage'])  
    mylistin = zip(news, descr, imgi)  
    return render(request, 'index.html',context={'mylist':mylistin})  
