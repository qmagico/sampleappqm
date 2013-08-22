from django.test import TestCase
from core.home.models import *

__author__ = 'tony'


class MessageTest(TestCase):
    def test_persist_message(self):
        m = Mensagem()
        m.conteudo = 'oi'
        m.save()
        m = Mensagem.objects.all()[0]
        self.assertEqual('oi', m.conteudo)