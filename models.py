from google.appengine.ext import ndb


class Message(ndb.Model):
    sender = ndb.StringProperty()
    recipient = ndb.StringProperty()
    subject = ndb.StringProperty()
    datetime = ndb.DateTimeProperty(auto_now_add=True)
    body = ndb.StringProperty()


class User(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
