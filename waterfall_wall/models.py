# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
import django_pgjsonb


class Feed(models.Model):
    id = models.BigIntegerField(primary_key=True)
    article_id = models.BigIntegerField(unique=True)
    article_json = django_pgjsonb.JSONField()

    class Meta:
        db_table = 'feed'


class Image(models.Model):
    article = models.ForeignKey(Feed, blank=True, null=True)
    url = models.TextField()
    nude_percent = models.IntegerField(blank=True, null=True)
    path = models.ImageField(null=True)

    class Meta:
        db_table = 'image'
        unique_together = (('url', 'article'),)
