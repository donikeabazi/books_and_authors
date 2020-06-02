from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('authors', views.authors),
    path('books/<int:id>', views.book, name='book'),
    path('authors/<int:id>', views.author, name='author')
]