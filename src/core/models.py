# coding: UTF-8
from django.db import models
# from django.utils import timezone
# from datetime import timedelta
# from django.contrib.auth.models import User
# import hashlib, time, random
# from core.utils.frespo_utils import get_or_none
# from social_auth.models import UserSocialAuth
# from django.utils.http import urlquote
# from django.template.defaultfilters import slugify
# from django.dispatch import receiver
# from emailmgr.signals import user_activated_email
# from decimal import Decimal
# from core.utils.frespo_utils import twoplaces
# from bitcoin_frespo.models import *
# from frespo_currencies import currency_service
# from django.conf import settings

class Mensagem(models.Model): 
    conteudo = models.TextField(null=False, blank=False)

