from django.urls import path

from rarestudy.views import homeView

urlpatterns = [
    ## home
    path('', homeView.index, name='index'),
]