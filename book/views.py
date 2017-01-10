from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Book
from .highlighting import Highlighter


class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'

    def get_queryset(self):
        result = super(BookListView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            result = Book.objects.search(query)
            highlight = Highlighter(query, html_tag='span', css_class='yellow', max_length=1000)
            for item in result:
                item.title = highlight.highlight(item.title)
                item.content = highlight.highlight(item.content)
        return result


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'

    def get_object(self):
        return get_object_or_404(Book, slug__iexact=self.kwargs['slug'])