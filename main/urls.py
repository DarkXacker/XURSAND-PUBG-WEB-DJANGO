from django.urls import *
from .views import *

urlpatterns = [
    path('', gameList, name='main'),
    path('game/<int:pk>/', GameDetailView.as_view(), name='game'),
]