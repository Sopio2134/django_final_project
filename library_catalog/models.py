from django.contrib.auth.models import AbstractUser
from django.db import models

class UserModel(AbstractUser):
    full_name = models.CharField(max_length=100)
    e_mail = models.EmailField(unique=True)
    unique_identifier = models.CharField(max_length=20, unique=True)
    birth_date = models.DateField()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='associated_users', 
        blank=True,
        help_text='List of user groups for classification or permission settings.'  
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='assigned_permissions', 
        blank=True,
        help_text='Permissions explicitly granted to this user for system access.'
    )
    def __str__(self):
        return self.username


# Author Model

class AuthorModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Book Author'

    def __str__(self):
        return self.name

# Category Model

class CategoryModel(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'Categorie'

    def __str__(self):
        return self.name

# Books Model

class BooksModel(models.Model):
    title = models.CharField(max_length=80)
    summary = models.TextField(max_length=2000)
    pdf = models.FileField(upload_to='pdfs/')
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    category = models.ManyToManyField(CategoryModel)
    published_date = models.DateField()
    in_stock = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Book'

    def __str__(self):
        return self.title