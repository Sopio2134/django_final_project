from django.contrib import admin
from .models import UserModel, AuthorModel, CategoryModel, BooksModel

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'e_mail', 'unique_identifier', 'birth_date')

@admin.register(BooksModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'in_stock')
    list_filter = ('category', 'author', 'published_date')
    search_fields = ('title', 'author')
    filter_horizontal = ('category',)

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



