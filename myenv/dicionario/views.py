from django.shortcuts import render
from .models import Word

def index(request):
    return render(request, 'dicionario/index.html', {})

def word_list(request):
    words = Word.objects.filter(word_pt__startswith='A').order_by('word_pt')
#    words = Word.objects.all()
    return render(request, 'dicionario/word_list.html', {'words': words})