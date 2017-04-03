"""version: 1.0"""

from jinja2 import Environment as env
from jinja2 import TemplateNotFound
from jinja2 import FileSystemLoader
from pip._vendor.lockfile import Error


class Template(object):
    path = None  # static class variable only set once for the entire application

    @staticmethod
    def self_render_template(filename, template_vars={}):
        """
        function to render a template for a given filename
        this function is
        :param filename: filename of the html script
        :param template_vars: template vars from outside
        :return: a HTML string of the rendered Template
        """
        #  path = os.getcwd()
        try:
            tmpl = env(loader=FileSystemLoader(Template.path))
            print (tmpl.loader.list_templates())

            tmpl = tmpl.get_template(filename)
        except TemplateNotFound, e:
            print(e.message)
            import cherrypy
            raise cherrypy.HTTPError(404, "No Site Founded on this server\n " + e.message)
        except Error, e:
            import cherrypy
            raise cherrypy.HTTPError(message=e.message)

        return tmpl.render(template_vars)
