from django.conf.urls import include, url
from posts import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        # url(r'^search/', views.search,name='search'),

        url(r'^nikos', views.demosearch, name='search_form'),
]