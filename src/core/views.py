import json
import urllib
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from core.models import *


def home(request):
    if 'token' in request.GET:
        token = request.GET['token']
        ns = request.GET['ns']
        url = "http://localhost:8081/api/auth/%s/%s" % (token, ns)
        user_data = urllib.urlopen(url).read()
        user_data = json.loads(user_data)
        request.session.update({'user_data': user_data})
    else:
        user_data = request.session.get('user_data')

    mensagens = Mensagem.objects.filter(user_id=user_data['user_id'])

    values = {'mensagens': mensagens, 'user_data': user_data}

    response = render_to_response('core/home.html',
                                  values,
                                  context_instance = RequestContext(request))

    return response


def nova_mensagem(request):
    user_data = request.session.get('user_data')
    msg = Mensagem()
    msg.conteudo = request.POST['conteudo']
    msg.user_id = user_data['user_id']
    msg.save()
    return redirect('/')
