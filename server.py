#!/usr/bin/env python

import webapp2
from google.appengine.ext import ndb
import logging


class Server(ndb.Model):
    ip = ndb.TextProperty()

server_name = "mini"
class ifconfig(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        server = Server.get_by_id(server_name)
        if server:
            self.response.write(server.ip)
        else:
            self.response.write("")

    def post(self):
        curr_ip = self.request.remote_addr
        server = Server.get_by_id(server_name)
        if server:
            server.ip = curr_ip
            server.put()
        else:
            server = Server(id="mini", ip=curr_ip)
            server.put()
        self.response.write(curr_ip)

logging.getLogger().setLevel(logging.DEBUG)

application = webapp2.WSGIApplication([
    ('/mini/ifconfig', ifconfig),
], debug=True)
