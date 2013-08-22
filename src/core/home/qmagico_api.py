import json
import urllib2
from google.appengine.api import urlfetch

__author__ = 'tony'


class QMApi():

    def __init__(self, host, appid, api_key):
        urlfetch.set_default_fetch_deadline(59)

        self.host = host
        self.appid = appid
        self.api_key = api_key

    def _do_get(self, url):
        req = urllib2.Request(url)
        req.add_header('api_key', self.api_key)
        req.add_header('appid', self.appid)
        resp = urllib2.urlopen(req)
        result = resp.read()
        result = json.loads(result)
        return result

    def auth(self, token, ns):
        url = "%s/api/auth/%s/%s" % (self.host, token, ns)
        return self._do_get(url)

    def content__get_by_type(self, ns, type=''):
        url = "%s/api/content/get_contents/%s/%s" % (self.host, ns, type)
        return self._do_get(url)

    def user__get_student_classes(self, ns, user_id):
        url = "%s/api/user/get_student_classes/%s/%s" % (self.host, ns, user_id)
        return self._do_get(url)

    def metrics__get_content_metrics(self, ns, user_id, content_id):
        url = "%s/api/metrics/get_content_metrics_from_user/%s/%s/%s" % (self.host, ns, user_id, content_id)
        return self._do_get(url)
