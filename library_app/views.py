from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, pagination, filters
from rest_framework.generics import ListCreateAPIView

from library_app.models import Book
from library_app.serializer import BookSeializer


#

# Create your views here.
class Books(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSeializer
    pagination_class = pagination.PageNumberPagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['category', 'Is_available']
    search_fields = ['Title', 'Author']

class Books_RUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSeializer
