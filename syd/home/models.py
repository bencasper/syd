# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsnippets.models import register_snippet


class HomePage(Page):
    pass


@register_snippet
class Category(models.Model):
    # don't use primary_key=True
    # category_id = models.IntegerField(verbose_name=u'分类ID', unique=True, db_index=True, null=False, blank=False)
    category_name = models.CharField(verbose_name=u'分类名称', max_length=255)

    panels = [
        FieldPanel('category_name'),
    ]

    api_fields = ['category_name', ]

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = u'商品分类'
        verbose_name_plural = u'商品分类'


@register_snippet
class Store(models.Model):
    store_name = models.CharField(verbose_name=u'电商名称', db_index=True, null=False, blank=False, max_length=255)
    product_detail_base_path = models.URLField(verbose_name=u'商品详情页基本URL')

    panels = [
        FieldPanel('store_name'),
        FieldPanel('product_detail_base_path'),
    ]

    api_fields = ['store_name', 'product_detail_base_path']

    def __str__(self):
        return self.store_name

    class Meta:
        verbose_name = u'电商'
        verbose_name_plural = u'电商'


@register_snippet
class ProductBase(models.Model):
    sku_name = models.CharField(verbose_name=u'自定义名称', db_index=True, null=False, blank=False, max_length=255)
    category_id = models.ForeignKey('Category', related_name='+')
    brand = models.CharField(verbose_name=u'品牌', max_length=255)
    size = models.CharField(verbose_name=u'尺码', max_length=255)
    color = models.CharField(verbose_name=u'颜色', max_length=255)
    count = models.FloatField(verbose_name=u'片数')
    created_at = models.DateTimeField(verbose_name=u'创建时间', default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    panels = [
        FieldPanel('sku_name'),
        FieldPanel('category_id'),
        FieldPanel('brand'),
        FieldPanel('size'),
        FieldPanel('color'),
        FieldPanel('count'),
    ]

    def __str__(self):
        return self.sku_name

    class Meta:
        verbose_name = u'商品'
        verbose_name_plural = u'商品'


@register_snippet
class ProductStore(models.Model):
    sku_id = models.ForeignKey('ProductBase', related_name='+')
    sku_id_store = models.CharField(verbose_name=u'电商商品ID', max_length=255)
    sku_name_store = models.CharField(verbose_name=u'电商商品名称', max_length=255)
    price = models.FloatField(verbose_name=u'价格')
    vip_price = models.FloatField(verbose_name=u'会员价')
    tax = models.FloatField(verbose_name=u'税费')
    img = models.ImageField(verbose_name=u'商品图片')
    store_id = models.ForeignKey('Store', related_name='+')
    store_name = models.CharField(verbose_name=u'电商名称', max_length=255)
    detail_url = models.URLField(verbose_name=u'详情页地址')
    availability = models.BooleanField(verbose_name=u'是否有货')
    created_at = models.DateTimeField(verbose_name=u'创建时间', default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    panels = [
        FieldPanel('sku_name_store'),
        FieldPanel('price'),
        FieldPanel('vip_price'),
        FieldPanel('tax'),
        FieldPanel('img'),
        FieldPanel('store_name'),
        FieldPanel('detail_url'),
        FieldPanel('availability'),
    ]

    def __str__(self):
        return self.store_name + self.sku_name_store

    class Meta:
        verbose_name = u'电商价格'
        verbose_name_plural = u'电商价格'

@register_snippet
class ProductPromotion(models.Model):
    sku_id_store = models.ForeignKey('ProductStore', related_name='+')
    sku_name_store = models.CharField(u'电商商品名称', max_length=255)
    store_name = models.CharField(verbose_name=u'电商名称', max_length=255)
    promotion_type = models.CharField(u'促销类型', max_length=255)
    promotion_desc = models.CharField(u'促销内容', max_length=255)

    panels = [
        FieldPanel('store_name'),
        FieldPanel('sku_name_store'),
        FieldPanel('promotion_type'),
        FieldPanel('promotion_desc')
    ]

    def __str__(self):
        return self.store_name + self.sku_name_store + self.promotion_desc

    class Meta:
        verbose_name = u'促销信息'
        verbose_name_plural = u'促销信息'




