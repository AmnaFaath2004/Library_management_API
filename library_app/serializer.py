from rest_framework import serializers

from library_app.models import Book


class BookSeializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
