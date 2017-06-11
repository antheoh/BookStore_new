import codecs

from django.shortcuts import render
import json
from urllib.request import urlopen
#from posts.models import Cart

from suds.client import Client
client = Client('http://localhost:9365/Bookstore/services/RetrieveBook?wsdl')


from django.http import HttpResponse
from django.template import loader,Context
from django.contrib.flatpages.models import FlatPage
from carton.cart import Cart


# Create your views here.
def index(request):
    cart = Cart(request)
     # data = json.load(urlopen('http://jsonplaceholder.typicode.com/posts'))
     # context = {'posts' : data}
     # return render(request, 'allposts.html', context)

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

def buy_book(request):
    name=request.GET['name']
    if name is None:
        print("den diavazei to name")
    else :
        print("to nama einai iso me "+name)
    client.service.recude_quantity(name)
    response_data = {'title': name}

    context = {'data': response_data}

    return render(request, 'buy.html', context)


def demosearch(request):

    book = request.GET['q']

    # EDW KALEIS TO SOAP DINONTAS TITLO MESA APO TO Q KAI PERNONTAS PISW TO ID GIA NA TO XRHSIMOPOIHSEIS PARAKATW!

    id = client.service.show_book(book)
    if id is None:
        print("null value")
    else :
        print("to id einai iso me"+id)

    reader=codecs.getreader("UTF-8")


    data = json.load(reader(urlopen('https://www.googleapis.com/books/v1/volumes?q=' + str(id))))


     #info = []
     #k = 0
     #for i in data["items"]:
     #    title = {'index': k, title: i[k]["volumeInfo"]["title"]}
     #    info.append(title)
     #    k += 1

     #all_titles = info


    try :
        id = data["items"][0]["id"]
    except KeyError as e:
        id='-'

    try:
        title = data["items"][0]["volumeInfo"]["title"]
    except KeyError as e:
        title='-'

    try :
        Authors=data["items"][0]["volumeInfo"]["authors"]
    except KeyError as e:
        Authors='-'

    try :
        Publisher = data["items"][0]["volumeInfo"]["publisher"]
    except KeyError as e:
        Publisher='-'

    try :
        Category = data["items"][0]["volumeInfo"]["categories"]
    except KeyError as e:
        Category= '-'

    try :
        Price=data["items"][0]["saleInfo"]["listPrice"]["amount"]
    except KeyError as e:
        Price='-'

    try :
        AverageRating=data["items"][0]["items"][0]["AverageRating"]
    except KeyError as e:
        AverageRating='-'

    response_data = {'id':id, 'title':title,'book':book,'Authors':Authors,'Publisher':Publisher,'Category':Category,'Price':Price,'AverageRating':AverageRating}


    context = {'data':response_data}

    return render(request, 'result.html', context)







   # response_data = {'id':isbn,'title':book}

   # context = {'data': response_data}

   # return render(request, 'result.html', context)

