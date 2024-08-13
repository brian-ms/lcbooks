from django.contrib import admin
from .models import Book, Review


# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    # class to change how the books are
    # displayed in the django admin page,
    # adding the additional fields to
    # make them displayed.
    inlines = [
        ReviewInline,
    ]
    list_display = (
        "title",
        "author",
        "price",
    )


admin.site.register(Book, BookAdmin)
