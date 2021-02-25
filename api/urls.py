from django.urls import path
from .views import Test, article_list

urlpatterns = [
    path('', Test, name="test"),
    path('articles/', article_list, name="articles")
]
