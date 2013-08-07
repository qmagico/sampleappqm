from core import qmagico_api
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from core.models import *


def getQMApi():
    host = Config.get('qmagico_host', 'http://localhost:8080')
    api_key = Config.get('qmagico_api_key', 'abc123')
    return qmagico_api.QMApi(host, api_key)


def authenticate(request):
    token = request.GET['token']
    ns = request.GET['ns']
    qmapi = getQMApi()
    user_data = qmapi.auth(token, ns)
    if 'error' in user_data:
        raise BaseException()
    request.session.update({'user_data': user_data})


def home(request):
    if 'token' in request.GET:
        authenticate(request)
        
    user_data = request.session.get('user_data')

    mensagens = Mensagem.objects.all()
    if user_data:
        mensagens = mensagens.filter(user_id=user_data['user_id'])

    values = {'mensagens': mensagens, 'user_data': user_data}

    response = render_to_response('core/home.html',
                                  values,
                                  context_instance=RequestContext(request))

    return response


def nova_mensagem(request):
    user_data = request.session.get('user_data')
    msg = Mensagem()
    msg.conteudo = request.POST['conteudo']
    if user_data:
        msg.user_id = user_data['user_id']
    msg.save()
    return redirect('/')
