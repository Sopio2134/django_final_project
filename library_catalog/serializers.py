from rest_framework import serializers
from .models import AuthorModel, CategoryModel, BooksModel

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'

class BooksSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=AuthorModel.objects.all())
    category = serializers.StringRelatedField(many=True)  # Use StringRelatedField to return category names

    class Meta:
        model = BooksModel
        fields = '__all__'

    def create(self, validated_data):
        categories = validated_data.pop('category')  
        book = Book.objects.create(**validated_data)  
        book.category.set(categories)  
        return book

    def update(self, instance, validated_data):
        categories = validated_data.pop('category', None)  
        for attr, value in validated_data.items():
            setattr(instance, attr, value)  
        if categories is not None:
            instance.category.set(categories)  
        instance.save()  
        return instance