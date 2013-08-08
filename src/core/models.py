# coding: UTF-8
from django.db import models
from django.db.models import fields


class Mensagem(models.Model): 
    conteudo = models.TextField(null=False, blank=False)
    user_id = fields.CharField(null=False, max_length=64)


class Config(models.Model):
    name = fields.CharField(null=False, max_length=64)
    value = fields.CharField(null=False, max_length=512)

    @classmethod
    def get(cls, name, default_value=''):
        try:
            config = cls.objects.get(name=name)
        except cls.DoesNotExist:
            config = Config(name=name, value=default_value)
            config.save()
        return config.value