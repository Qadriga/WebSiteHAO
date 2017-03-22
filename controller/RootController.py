"""Version:1.0"""

import cherrypy
import os
import model.template as template
import imp
import sys


class RootController(object):

    def __init__(self):
        cwd = os.getcwd()

        if os.name is 'nt':
            self.html_dir = "\\view\\"
            self.module_dir = cwd + "\\model\\request_functions\\"
            self.files = os.listdir(cwd + self.html_dir + "\\sites\\")
            # list all files in the sites folder and make them callable
        elif os.name is 'posix':
            self.html_dir = "/view/"
            self.module_dir = cwd + "/model/request_functions/"
            self.files = os.listdir(cwd + self.html_dir + "/sites/")
            # list all files in the sites folder and make them callable
        else:
            return
        template.Template.path = cwd + self.html_dir  # set path for templates
        self.py_files = os.listdir(self.module_dir)
        del self.py_files[0]  # remove __init__.py from list
        self._import_modules()
        print self.files
        print self.py_files
        return

    @cherrypy.expose
    def index(self):
        return template.Template.self_render_template("sites/index.html")

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
            cherrypy.request.params['name'] = vpath.pop(0)
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
            return template.Template.self_render_template("sites/" + name + ".html")
        else:
            raise cherrypy.HTTPError(404, "Nothing founded on this Server")

    @cherrypy.expose
    def post_expose(self, post_name, *args, **kwargs):
        """
        :param post_name: name of the post request
        :param args: additional arguments
        :param kwargs: additional keyword arguments
        :return:
        """
        if kwargs['name'] is 'post':
            return "Post Expose"
        else:
            raise cherrypy.HTTPError(404)

    def find_function(self, function_name, filename=None):
        """
        find a function which matches to function name
        :param function_name: function name to find
        :param filename: filename where the function can be founded
        :return: function which matches to the given function name
        """

    def _import_modules(self):
        """
        wrapper function to import all functions founded at request_functions
        :return:
        """
        import module as mlib
        func_names = list()
        module_names = list()
        for file_name in self.py_files:
            module_name = os.path.splitext(file_name)[0]
            try:
                module = __import__('model.request_functions.' + module_name, globals(), locals(), func_names, -1)
                print dir(module)
            except ImportError:
                pass
            module_names.append(module_name)
        print module_names

    @staticmethod
    def my_import(self, module_name, func_names=[], cache=False):
        if module_name in globals() and cache:
            return True
        try:
            m = __import__(module_name, globals(), locals(), func_names, -1)
            if func_names:
                for func_name in func_names:
                    globals()[func_name] = getattr(m, func_name)
            else:
                globals()[module_name] = m
            return True
        except ImportError:
            return False

    @staticmethod
    def my_imports(modules):
        for module in modules:
            if type(module) is tuple:
                name = module[0]
                funcs = module[1]
            else:
                name = module
                funcs = []
            if not RootController.my_import(name, funcs):
                return module
        return ''

    @staticmethod
    def check_Plugins_Imports(plugin, modules):
        c = RootController.my_imports(modules)
        if c:
            print plugin + " has errors!: module '" + c + "' not found"
