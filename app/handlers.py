import jinja2

# set default template directory
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('app/templates'))

# load custom libraries
from lib.basehandler import BaseHandler


class LanguageEntryHandler(BaseHandler):
    def get(self, language):
        #"""Set language for the session based on language code appended to url"""

        BaseHandler.set_language(self, language)
        self.redirect_to('home')


class HomeHandler(BaseHandler):
    def get(self):
        """Display the Home page"""

        template_values = {
            # declare template values here
            'l10n': BaseHandler.get_content(self)
        }

        # load the welcome page template
        template = jinja_env.get_template('index.html')

        # display page
        self.response.out.write(template.render(template_values))


class ChangeLanguageHandler(BaseHandler):
    def get(self):
        """Change the site language"""

        new_language = self.request.get('lang')

        BaseHandler.set_language(self, new_language)

        # redirect user back to their previous page
        self.redirect(self.request.referer)
