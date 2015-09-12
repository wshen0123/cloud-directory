#!/usr/bin/env python

import webapp2
from google.appengine.ext import ndb
import logging


class Host(ndb.Model):
    ip = ndb.TextProperty()

class ifconfig(webapp2.RequestHandler):
    def get(self, hostname):
        self.response.headers['Content-Type'] = 'text/plain'

        host = Host.get_by_id(hostname)
        if host:
            self.response.write(host.ip)
        else:
            self.response.write("")

    def post(self, hostname):
        curr_ip = self.request.remote_addr
        host = Host.get_by_id(hostname)
        if host:
            host.ip = curr_ip
            host.put()
        else:
            host = Host(id=hostname, ip=curr_ip)
            host.put()
        self.response.write(curr_ip)

logging.getLogger().setLevel(logging.DEBUG)

application = webapp2.WSGIApplication([
    webapp2.Route(r'/<hostname>/ip', handler=ifconfig, name='ifconfig')
], debug=True)
