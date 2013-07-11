import json
import os
import webapp2
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

    def get_arb(self, page_name=''):
        language = self.get_language()

        if page_name == '':
            page = language
        else:
            page = page_name

        arb = json.load(open('app/l10n/' + language + '/' + page + '.arb'))
        return arb

    def get_data_variables(self):
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

        return data

    def get_content(self, page_name=''):
        # data_variables = self.get_data_variables(page_name)
        language = self.get_language()

        if page_name == '':
            page = language
        else:
            page = page_name

        arb = self.get_arb(page)
        copydeck = {}

        for key, value in arb.iteritems():
            if '@' in key:
                continue

            placeholders = arb['@' + key]['placeholders']

            replacements = {}
            for placeholder in placeholders:
                replacement = arb['@' + key]['placeholders'][placeholder]['example']
                replacements[placeholder] = replacement

            value = value.format(**replacements)
            copydeck[key] = value

        # if data_variables is not None:
        #     content = dict(copydeck.items() + data_variables.items())
        #     return content
        # else:
        return copydeck

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
