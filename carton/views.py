from django.shortcuts import render

from .models import Foo

# Create your views here.

def some_name(request):
    foo_instance=Foo.objects.create(name='test')
    return render(request,'test.html.htnl')


