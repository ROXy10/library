from django.db import models
from django.core.urlresolvers import reverse

from autoslug import AutoSlugField
from djorm_pgfulltext.models import SearchManager
from djorm_pgfulltext.fields import VectorField

class Book(models.Model):
    """Book Model"""

    title = models.CharField(max_length=255, blank=False, verbose_name="Title", null=True)
    slug = AutoSlugField(populate_from='title', editable=True)
    content = models.TextField(verbose_name="Content", blank=False, null=True)
    published = models.BooleanField(default=False, verbose_name="Published")
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Date updated", null=True)

    search_index = VectorField()

    objects = SearchManager(
        fields=('title', 'content'),
        config='pg_catalog.english',
        search_field='search_index',
        auto_update_search_field=True
    )

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

