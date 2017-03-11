"""Version:1.0"""

import cherrypy
import os
import model.template as template
import imp


class RootController(object):

    def __init__(self):
        cwd = os.getcwd()

        if os.name is 'nt':
            self.html_dir = cwd + "\\view\\"
            self.module_dir = cwd + "\\model\\"
        elif os.name is 'posix':
            self.html_dir = cwd + "/view/sites/"
            self.module_dir = cwd + "/model/"
        else:
            return
        self.files = os.listdir(self.html_dir)  # list all files in the sites folder and make them callable
        self.py_files = os.listdir(self.module_dir)
        del self.py_files[0]
        print self.files
        print self.py_files
        return

    @cherrypy.expose
    def index(self):
        return template.Template.self_render_template(self.html_dir + "index.html")

    def _cp_dispatch(self, vpath):
        """

        :param vpath: URL path info broken into its segments as list
        :return:
        """
        if len(vpath) == 1:
            cherrypy.request.params['name'] = vpath.pop()
            return self.file_expose
        elif len(vpath) == 2:
            cherrypy.request.params['post_name'] = vpath.pop(1)
            return self.post_expose
        return vpath

    @cherrypy.expose
    def file_expose(self, name, *args, **kwargs):
        """
        :param name: name of the requested html document
        :param args: additional arguments
        :param kwargs: additional keyword arguments
        :return:
        """
        print name
        if (name + ".html") in self.files:
            return template.Template.self_render_template(self.html_dir + name + ".html")
        else:
            raise cherrypy.HTTPError(404, "Nothing founded on this Server")

    @cherrypy.expose
    def post_expose(self, post_name, *args, **kwargs):
        """
        :param name: name of the post request
        :param args: additional arguments
        :param kwargs: additional keyword arguments
        :return:
        """
        return "Post Expose"
