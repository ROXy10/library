from django.contrib import admin


from .models import Book


class BookModelAdmin(admin.ModelAdmin):
    list_display = ["title", "published", "updated"]
    list_display_links = ["title", "published", "updated"]
    list_filter = ["updated", "published"]
    prepopulated_fields = {"slug": ("title",)}

    search_fields = ["title", "content"]

    class Meta:
        model = Book


admin.site.register(Book, BookModelAdmin)