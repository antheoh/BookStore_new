from django.shortcuts import render
import json
from urllib.request import urlopen

from suds.client import Client
client = Client('http://localhost:9365/Bookstore/services/RetrieveBook?wsdl')


from django.http import HttpResponse
from django.template import loader,Context
from django.contrib.flatpages.models import FlatPage



# Create your views here.
def index(request):
     data = json.load(urlopen('http://jsonplaceholder.typicode.com/posts'))
     context = {'posts' : data}
     return render(request, 'allposts.html', context)

def get_isbn(title):
    return client.service.show_book(title)


def search(request):

    query = request.GET['q']
    print('mpike mesa')
    results=FlatPage.objects.filter(content_incontains=query)
    t = loader.get_template('templates/name.html')
    c = Context({ 'query': query,'results':results})

    response=t.render(c)
    return HttpResponse(response)

def demosearch(request):

    book = request.GET['q']

    # EDW KALEIS TO SOAP DINONTAS TITLO MESA APO TO Q KAI PERNONTAS PISW TO ID GIA NA TO XRHSIMOPOIHSEIS PARAKATW!

    isbn = client.service.show_book(book)
    if isbn is None:
        print("null value")
    else :
        print(isbn)


    #data = json.load(urlopen('https://www.googleapis.com/books/v1/volumes?q=' + str(21)))

    # info = []
    # k = 0
    # for i in data["items"]:
    #     title = {'index': k, title: i[k]["volumeInfo"]["title"]}
    #     info.append(title)
    #     k += 1
    #
    # all_titles = info

#--

    #id = data["items"][0]["id"]
    #title = data["items"][0]["volumeInfo"]["title"]

    #response_data = {'id':id, 'title':title,'book':book}


    #context = {'data':response_data}






    response_data = {'id':isbn,'title':book}

    context = {'data': response_data}

    return render(request, 'demo.html', context)

