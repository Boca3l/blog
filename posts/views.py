from django.shortcuts import render

dados_post = {
    1: {
        'title': 'Seu Madruga',
        'description': 'Seu Madruga felizao',
        'autor': 'Predo',
        'date': '01/01/2021',
        'tags': {'tag1', 'tag2', 'tag3'},
        'comments': {'autor1':'coment1','autor2':'coment2','autor2':'coment3'},
    },
    2:{
        'title': 'Nicolas Cage',
        'description': 'Nicolas Cage felizao',
        'autor': 'Predo',
        'date': '01/01/2021',
        'tags': {'tag4', 'tag5', 'tag6'},
        'comments': {'autor1':'coment1','autor2':'coment2','autor2':'coment3'},
    },
    3:{
        'title': 'Padre Marcelo',
        'description': 'Padrão das Massas',
        'autor': 'Predo',
        'date': '01/01/2021',
        'tags': {'tag7', 'tag8', 'tag9'},
        'comments': {'autor1':'coment1','autor2':'coment2','autor2':'coment3'},
    }
}

# Create your views here.
def index(request):
    return render(request, 'posts/index.html',{'posts': dados_post})
