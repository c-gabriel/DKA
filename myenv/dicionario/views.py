from django.shortcuts import render
from .models import Word
from django.http import HttpResponse
import json

def index(request):
    return render(request, 'dicionario/index.html', {})

def busca(request):
    return render(request, 'dicionario/busca.html', {})

def dicionario(request):
    return render(request, 'dicionario/dicionario.html', {})

def sobre(request):
    return render(request, 'dicionario/sobre.html', {})

def contato(request):
    return render(request, 'dicionario/contato.html', {})

def pt(request):
    return render(request, 'dicionario/pt.html', {})

def en(request):
    return render(request, 'dicionario/en.html', {})

def cr(request):
    return render(request, 'dicionario/cr.html', {})

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        words = Word.objects.filter(word_pt=q)
        return render(request, 'dicionario/search.html', {'words': words})
    else:
        return HttpResponse('Please submit a search term.')
    
def word_list_pt(request,q):
    letra = q
    words = Word.objects.filter(word_pt__istartswith=q).order_by('word_pt')
    return render(request, 'dicionario/word_list_pt.html', {'words': words, 'letra': letra})

def word_list_en(request,q):
    letra = q
    words = Word.objects.filter(word_pt__istartswith=q).order_by('word_en')
    return render(request, 'dicionario/word_list_en.html', {'words': words, 'letra': letra})

def word_list_cr(request,q):
    letra = q
    words = Word.objects.filter(word_pt__istartswith=q).order_by('word_cr')
    return render(request, 'dicionario/word_list_cr.html', {'words': words, 'letra': letra})
