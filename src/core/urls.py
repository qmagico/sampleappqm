from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.views.generic.simple import redirect_to

urlpatterns = patterns('core.home.views',
    url(r'^$', 'home'),
    url(r'^add$', 'nova_mensagem'),
    url(r'^mensagens$', 'mensagens')
)
