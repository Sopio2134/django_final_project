# library_catalog/tests.py
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import BooksModel, AuthorModel, CategoryModel

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create an author instance
        author = AuthorModel.objects.create(name="Jon Doe")
        
        # Create a category instance
        category = CategoryModel.objects.create(name="Fiction")
        
        # Simulate a file upload for the pdf field
        pdf_file = SimpleUploadedFile("sample.pdf", b"file_content", content_type="application/pdf")

        # Create a book instance
        cls.book = BooksModel.objects.create(
            title="A title",
            summary="An excellent summary of the book",
            pdf=pdf_file,  # Assign the simulated file to the pdf field
            author=author,
            published_date="2024-11-01",
            in_stock=10,
        )
        
        # Add the category to the book
        cls.book.category.add(category)

    def test_book_content(self):
        """Test the fields of the book model."""
        self.assertEqual(self.book.title, "A title")
        self.assertEqual(self.book.summary, "An excellent summary of the book")
        self.assertEqual(self.book.author.name, "Jon Doe")
        self.assertEqual(self.book.published_date, "2024-11-01")
        self.assertEqual(self.book.in_stock, 10)

    def test_book_listview(self):
        """Test the book list view."""
        response = self.client.get(reverse("book-lists"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A title")
        self.assertContains(response, "Fiction")  # Assuming category name appears in the view

    def test_book_detailview(self):
        """Test the book detail view."""
        response = self.client.get(reverse("book-details", kwargs={"pk": self.book.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A title")
        self.assertContains(response, "An excellent summary of the book")
