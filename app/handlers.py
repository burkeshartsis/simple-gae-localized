import jinja2

# set default template directory
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('app/templates'))

# load custom libraries
from lib.basehandler import BaseHandler

class HomeHandler(BaseHandler):
    def get(self):

        """Display the Home page"""

        template_values = {
            # declare template values here
        }

        # load the welcome page template
        template = jinja_env.get_template('index.html')

        # display page
        self.response.out.write(template.render(template_values))