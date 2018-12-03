# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.text import slugify
from easy_thumbnails.fields import ThumbnailerImageField


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=400, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Article(models.Model):
    FILE_PATH = 'static/images/blog/'

    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300, blank=False)
    content = models.TextField()
    image = ThumbnailerImageField(_('Imagen de fondo'), upload_to=FILE_PATH, max_length=1024,
                                  help_text=_("Podemos aceptar los siguientes formatos de imagen: .jpg, .gif, o .png."),
                                  null=True, blank=True)

    tags = models.CharField(max_length=100, blank=True, null=True)

    slug = models.CharField(max_length=400, blank=True)
    meta_title = models.CharField(default="", max_length=600, blank=True)
    meta_keywords = models.CharField(default="", max_length=600, blank=True)
    meta_description = models.CharField(default="", max_length=600, blank=True)
    views = models.IntegerField(default=0)

    user = models.ForeignKey(User, related_name='articles')

    is_published = models.BooleanField(default=False)

    category = models.ForeignKey(Category, blank=True, null=True)

    def split_tags(self):
        return self.tags.split(',')

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"

    def calculate_slug(self):
        slug = slugify(self.title)
        found = Article.objects.filter(slug=slug)
        if len(found) == 1:
            if found[0].slug == self.slug:
                return slug
        while len(Article.objects.filter(slug=slug)) > 0:
            slug = slugify(self.title) + str(self.objects.all().count() + 1)
            return slug
        return slug

    def save(self, **kwargs):
        if not self.pk:
            self.slug = self.calculate_slug()
        super(Article, self).save()

    class Meta:
        ordering = ('-date',)

    def __unicode__(self):
        return self.title



class MailList(models.Model):
    email = models.EmailField()

