from rest_framework import generics
from .models import BooksModel, AuthorModel, CategoryModel
from .serializers import BooksSerializer, AuthorSerializer, CategorySerializer

class BaseListCreateView(generics.ListCreateAPIView):
    """
    A base view class to handle list and create actions for a given model.
    """
    queryset = None
    serializer_class = None

class BaseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    A base view class to handle retrieve, update, and destroy actions for a given model.
    """
    queryset = None
    serializer_class = None

# Books views
class BookLists(BaseListCreateView):
    queryset = BooksModel.objects.all()
    serializer_class = BooksSerializer

class BookDetails(BaseRetrieveUpdateDestroyView):
    queryset = BooksModel.objects.all()
    serializer_class = BooksSerializer

# Author views
class AuthorLists(BaseListCreateView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetails(BaseRetrieveUpdateDestroyView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer

# Category views
class CategoryLists(BaseListCreateView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class CategoryDetails(BaseRetrieveUpdateDestroyView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
