#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import jinja2
import webapp2


from models import Message, User


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        # if params is None:
        #     params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))



class MainHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template("index.html", params=params)

class InboxHandler(BaseHandler):
    def get(self):
        messages = Message.query(Message.recipient = user.email).fetch()
        params = {"messages": messages}
        return self.render_template("inbox.html", params=params)

class OutboxHandler(BaseHandler):
    def get(self):
        messages = Message.query(Message.sender = user.email).fetch()
        params = {"messages": messages}
        return self.render_template("outbox.html", params=params)

class MessageViewHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template("message.html", params=params)

class MessageDeleteHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template("delete.html", params=params)

    def post(self):
        pass

class MessageNewHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template("new.html", params=params)

    def post(self):
        pass

class WeatherHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template("weather.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/inbox', InboxHandler),
    webapp2.Route('/outbox', OutboxHandler),
    webapp2.Route('/message/<message_id:\d+>', MessageViewHandler),
    webapp2.Route('/message/<message_id:\d+>/delete', MessageDeleteHandler),
    webapp2.Route('/new', MessageNewHandler),
    webapp2.Route('/weather', WeatherHandler),
], debug=True)
