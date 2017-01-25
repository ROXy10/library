from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'

    def get_queryset(self):
        result = super(BookListView, self).get_queryset()
        query = self.request.GET.get('query')
        if query:
            result = Book.objects.search(
                query,
                headline_field='content',
                headline_document='title',
                max_fragment=250
            ).search(
                query,
                headline_field='content',
                headline_document='content',
                max_fragment=250)
        return result


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'

    def get_object(self):
        return get_object_or_404(Book, slug__iexact=self.kwargs['slug'])