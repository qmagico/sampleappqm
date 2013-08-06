import json
import urllib2

__author__ = 'tony'


class QMApi():

    def __init__(self, host, api_key):
        self.host = host
        self.api_key = api_key

    def auth(self, token, ns):
        url = "%s/api/auth/%s/%s" % (self.host, token, ns)
        req = urllib2.Request(url)
        req.add_header('api_key', self.api_key)
        resp = urllib2.urlopen(req)
        user_data = resp.read()
        user_data = json.loads(user_data)
        return user_data
