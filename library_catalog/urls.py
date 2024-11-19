from django.urls import path
from .views import (
    BookLists,
    BookDetails,
    CategoryLists,
    CategoryDetails,
    AuthorLists,
    AuthorDetails
)

urlpatterns = [
    path('books/', BookLists.as_view(), name='book-lists'),
    path('books/<int:pk>/', BookDetails.as_view(), name='book-details'),
    path('categories/', CategoryLists.as_view(), name='category-lists'),
    path('categories/<int:pk>/', CategoryDetails.as_view(), name='category-details'),
    path('authors/', AuthorLists.as_view(), name='author-lists'),
    path('authors/<int:pk>/', AuthorDetails.as_view(), name='author-details'),
]