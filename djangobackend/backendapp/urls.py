from django.urls import path 
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('detailview/',views.detailview,name='detailview')
]