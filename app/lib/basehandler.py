import webapp2

class BaseHandler(webapp2.RequestHandler):
    """
        BaseHandler for all requests

        Holds the session properties so they
        are reachable for all requests
    """