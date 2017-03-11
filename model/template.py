"""version: 1.0"""

from jinja2 import Template as Template_jinja
from jinja2 import Environment as env
from jinja2 import TemplateNotFound
from jinja2 import FileSystemLoader
import os

from pip._vendor.lockfile import Error


class Template(object):

    @staticmethod
    def self_render_template(filename, template_vars={}):
        """
        function to render a template for a given filename
        this function is
        :param filename: filename of the html script
        :param template_vars: template vars from outside
        :return: a HTML string of the rendered Template
        """
        path, name = os.path.split(filename)
        try:
            tmpl = env(loader=FileSystemLoader(path or './')).get_template(name)
        except TemplateNotFound:
            import cherrypy
            raise cherrypy.HTTPError(404, "No Site Founded on this server")
        except Error, e:
            import cherrypy
            raise cherrypy.HTTPError(message=e.message)

        return tmpl.render(template_vars)
