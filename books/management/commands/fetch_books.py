# Fetch books from openlibrary using open library api
from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    help = "Fetches books from open Library and adds them to the database"

    def handle(self, *args, **kwargs):
        self.fetch_books()

    def fetch_books(self):
        search_term = "Pride and Prejudice"
        url = f"https://openlibrary.org/search.json?title={search_term}"

        response = request.get(url)
        data = response.json()
        books = data.get("docs", [])

        for book_data in books:
            title = book_data.get("title")
            author = book_data.get("author_name", ["Unknown Author"])[0]
            isbn = book_data.get("isbn", [None])[0]
            cover_url = (
                f"http://covers.openlibrary.org/b/isbn/{isbn}-L.jpg" if isbn else None
            )
            publish_date = book_data.get("first_publish_year", "Unknown")
            description = book_data.get("subtitle", "")

            if isbn and not Book.objects.filter(isbn=isbn).exists():
                book = Book(
                    title=title,
                    author=author,
                    isbn=isbn,
                    cover_url=cover_url,
                    publish_date=publish_date,
                    description=description,
                )
                book.save()
                self.stdout.write(
                    self.style.SUCCESS(f"Book '{title}' added successfully!")
                )
            else:
                self.stdout.write(f"Book '{title}' already exists in the database.")
