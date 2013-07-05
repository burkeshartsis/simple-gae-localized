from webapp2_extras.routes import RedirectRoute

# load custom libraries
from lib.basehandler import BaseHandler
import handlers

_routes = [
    RedirectRoute('/', handlers.HomeHandler, name='home', strict_slash=True),
    RedirectRoute('/change-language', handlers.ChangeLanguageHandler, name='change_language', strict_slash=True),
    RedirectRoute('/<language>', handlers.LanguageEntryHandler, name='enter_with_language', strict_slash=True)
]


def get_routes():
    return _routes


def add_routes(app):
    for r in _routes:
        app.router.add(r)
