from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.

def Test(request):
    return HttpResponse("Hello")


def article_list(request):

    # Get all articles
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return  JsonResponse(serializer.data, safe=False)