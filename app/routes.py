from webapp2_extras.routes import RedirectRoute
import handlers


_routes = [
    RedirectRoute('/', handlers.HomeHandler, name='home', strict_slash=True)
]


def get_routes():
    return _routes


def add_routes(app):
    for r in _routes:
        app.router.add(r)