import json
from core.home import qmagico_api
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from core.home.models import *


def getQMApi():
    host = Config.get('qmagico_host', 'http://localhost:8080')
    api_key = Config.get('qmagico_api_key', 'abc123')
    app_id = Config.get('qmagico_api_id', 'sampleapp')
    namespace = Config.get('namespace', 'www')
    return qmagico_api.QMApi(host, app_id, api_key, namespace)


def authenticate(request):
    token = request.GET['token']
    ns = request.GET['ns']
    qmapi = getQMApi()
    user_data = qmapi.auth(token, ns)
    if 'error' in user_data:
        raise BaseException()
    request.session.update({'user_data': user_data, 'namespace': ns})


def home(request):
    if 'token' in request.GET:
        authenticate(request)
    user_data = request.session.get('user_data')
    ns = request.session.get('namespace')
    qmapi = getQMApi()
    school_classes = qmapi.user__get_student_classes(ns, user_data['user_id'])

    contents = qmapi.content__get_by_type(ns)

    contents_length = {'VIDEO': 0, 'VIMEO': 0, 'EXERCISE_LIST': 0, 'TEXT_CLASS': 0}
    metrics_length = {'VIDEO': 0, 'VIMEO': 0, 'EXERCISE_LIST': 0, 'TEXT_CLASS': 0}

    for content in contents:
        contents_length[content['type']] += 1
        metric = qmapi.metrics__get_content_metrics(ns, user_data['user_id'], content['id'])
        if not metric:
            continue

        if not metric.get('error', False) and metric['status'] == "CORRECT":
            metrics_length[content['type']] += 1

    values = {
        'user_data': user_data,
        'metrics_length': metrics_length,
        'contents': contents,
        'contents_length': contents_length,
        'school_classes': school_classes
    }
    response = render_to_response('core/index.html',
                                  values,
                                  context_instance=RequestContext(request))
    return response


def mensagens(request):
    user_data = request.session.get('user_data')
    mensagens = Mensagem.objects.filter(user_id=user_data['user_id'])

    values = {'mensagens': mensagens,
              'user_data': user_data}

    response = render_to_response('core/messages.html',
                                  values,
                                  context_instance=RequestContext(request))
    return response


def nova_mensagem(request):
    user_data = request.session.get('user_data')
    msg = Mensagem()
    msg.conteudo = request.POST['conteudo']
    msg.user_id = user_data['user_id']
    msg.save()
    return redirect('/mensagens')
