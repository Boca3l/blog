from django.urls import path
from posts.views import index

urlpatterns = [
    path('', index, name='index'),
    # path('imagem/', imagem, name ='imagem'), exemplo
]