# -*- coding: utf-8 -*-

from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsnippets.models import register_snippet


class HomePage(Page):
    pass


@register_snippet
class Category(models.Model):

    categoryID = models.IntegerField(verbose_name=u'分类ID', unique=True, db_index=True, null=False, blank=False)
    categoryName = models.CharField(verbose_name=u'分类名称', max_length=255)

    panels = [
        FieldPanel('categoryName'),
        FieldPanel('categoryID'),
    ]

    api_fields = ['page', 'url', 'text']

    def __str__(self):
        return self.categoryName

    class Meta:
        verbose_name = u'商品分类'
        verbose_name_plural = u'商品分类'



