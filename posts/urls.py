from django.conf.urls import include, url
from posts import views


urlpatterns = [
        url(r'^$', views.index, name='index'),
        # url(r'^search/', views.search,name='search'),
        url(r'^search', views.demosearch, name='search_form'),
        url(r'^buy',views.buy_book, name='buy_book')]
