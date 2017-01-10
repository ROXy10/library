from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save

from djorm_pgfulltext.models import SearchManager
from djorm_pgfulltext.fields import VectorField

class Book(models.Model):
    """Book Model"""

    title = models.CharField(max_length=256, blank=False, verbose_name="Название", null=True)
    slug = models.SlugField(unique=True, null=True)
    content = models.TextField(verbose_name="Текст", blank=False, null=True)
    published = models.BooleanField(default=False, verbose_name="Опобликовано")
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Дата обновления", null=True)

    search_index = VectorField()

    objects = SearchManager(
        fields=('title', 'content'),
        config='pg_catalog.russian',
        search_field='search_index',
        auto_update_search_field=True
    )

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"
        ordering = ["title"]

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Book.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Book)
