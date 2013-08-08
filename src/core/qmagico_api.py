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

    def content__get_by_type(self, ns, type):
        url = "%s/api/content/get_by_type/%s/%s" % (self.host, ns, type)
        return self._do_get(url)
