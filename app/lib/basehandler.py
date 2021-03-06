import ast
import json
import os
import webapp2
from jinja2 import Template
from webapp2_extras import sessions


class BaseHandler(webapp2.RequestHandler):
    """
        BaseHandler for all requests

        Holds the session properties so they
        are reachable for all requests
    """
    def dispatch(self):
        """
            Get a session store for this request.
        """
        self.session_store = sessions.get_store(request=self.request)

        route_name = self.request.route.name

        # if this is not the home page or a translation
        if route_name != 'home' and route_name != 'enter_with_language':
            return self.redirect('/')

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session_store(self):
        return sessions.get_store(request=self.request)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

    def set_page_name(self, page_name=''):
        language = self.get_language()

        if page_name == '':
            page = language
        else:
            page = page_name

        return page

    def get_arb(self, page_name=''):
        language = self.get_language()
        page = self.set_page_name(page_name)

        arb = json.load(open('app/l10n/' + language + '/' + page + '.arb'))
        return arb

    def get_data_variables(self, output='raw'):
        language = self.get_language()

        try:
            global_variables = json.load(open('app/l10n/data.json'))
            localized_variables = json.load(open('app/l10n/' + language + '/data.json'))

            data = dict(global_variables.items() + localized_variables.items())
        except:
            try:
                data = json.load(open('app/l10n/' + language + '/data.json'))
            except:
                data = None

        if output == 'nested' and data is not None:
            data = {
                'data': data
            }

        return data

    def get_copydeck(self, page_name=''):
        page = self.set_page_name(page_name)

        arb = self.get_arb(page)
        copydeck = {}

        for key, value in arb.iteritems():
            if '@' in key:
                continue

            try:
                placeholders = arb['@' + key]['placeholders']
            except:
                placeholders = {}

            replacements = {}
            for placeholder in placeholders:
                replacement = arb['@' + key]['placeholders'][placeholder]['example']
                replacements[placeholder] = replacement

            value = value.format(**replacements)
            copydeck[key] = value

        return copydeck

    def get_content(self, page_name=''):
        page = self.set_page_name(page_name)

        copy = self.get_copydeck(page)
        data = self.get_data_variables('nested')

        if data is not None:
            template = Template(str(copy)).render(data)
            content = ast.literal_eval(template)
            return content
        else:
            return copy

    def get_languages(self):
        languages = os.listdir('app/l10n')
        return languages

    def set_language(self, selected_language):
        valid_languages = self.get_languages()
        new_language = ''

        # Make sure language is valid, otherwise set to English US
        if selected_language in valid_languages:
            new_language = selected_language

        else:
            new_language = 'en'

        self.session['user_language'] = new_language

    """ Return currently selected language """
    def get_language(self):
        if self.session.get('user_language'):
            language = self.session['user_language']
        else:
            language = 'en'
            self.set_language(language)

        return language
