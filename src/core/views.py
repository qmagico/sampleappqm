from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from core.models import *


def home(request):
    mensagens = Mensagem.objects.all()
    values = {'mensagens': mensagens}
    return render_to_response('core/home.html',
        values,
        context_instance = RequestContext(request))


def nova_mensagem(request):
    msg = Mensagem()
    msg.conteudo = request.POST['conteudo']
    msg.save()
    return redirect('/')
