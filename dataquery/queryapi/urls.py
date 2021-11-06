from django.urls import path

from . import apis

urlpatterns = [
    path('', apis.index, name='index'),
    path('search', apis.search, name='search')
]