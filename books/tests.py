from django.test import TestCase
from django.urls import reverse

from .models import Book

class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "A good Title",
            subtitle = "An Excelent Subtitle",
            author = "William Shakespear",
            isbn = 4567342589071,
        )
    
    def test_book_content(self):
        self.assertEqual(self.book.title, "A good Title")
        self.assertEqual(self.book.subtitle, "An Excelent Subtitle")
        self.assertEqual(self.book.author, "William Shakespear")
        self.assertEqual(self.book.isbn, 4567342589071)
    
    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "An Excelent Subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")



