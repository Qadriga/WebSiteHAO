"""Version:1.0"""

import cherrypy
import os
import model.template as template
import importlib
import controller.PostController
from model.database import Database
class RootController(object):

    def __init__(self):
        """
        constructor of this class
        """
        self._init_structure()

    def _init_structure(self):
        """
        class method for (re)loading the html structure and post-methods
        :return:
        """
        cwd = os.getcwd()
        if os.name is 'nt':
            self.html_dir = "\\html\\"
            self.module_dir = cwd + "\\model\\request_functions\\"
            self.files = os.listdir(cwd + self.html_dir + "\\sites\\")
            # list all files in the sites folder and make them callable
        elif os.name is 'posix':
            self.html_dir = "/html/"
            self.module_dir = cwd + "/model/request_functions/"
            self.files = os.listdir(cwd + self.html_dir + "/sites/")
            # list all files in the sites folder and make them callable
        else:
            return
        self.postController = controller.PostController.PostController(self.module_dir)  # pass path to Post Controller
        template.Template.path = cwd + self.html_dir  # set path for templates
        self.py_files = os.listdir(self.module_dir)
        del self.py_files[0]  # remove __init__.py from list
        self.py_files = self.remove_pyc_files(self.py_files)
        self._import_sites()
        # self._import_modules()
        print self.files
        print self.py_files
        return

    @staticmethod
    def remove_pyc_files(array=[]):
        """
        function to filter only .py files out from a list of filename
        :param array: array with to filter
        :return: new list of filename
        """
        new_array = []
        for element in array:
            extention = os.path.splitext(element)[1]
            if extention == '.py':
                new_array.append(element)
        return new_array

    @cherrypy.expose
    def index(self):
        temp_vars = dict()
        temp_vars.update({'terms': Database().query(table_name="terms", ordered_by="t_date desc")})
        return template.Template.self_render_template("sites/index.html", temp_vars)

    def _cp_dispatch(self, vpath):
        """

        :param vpath: URL path info broken into its segments as list
        :return:
        """
        if len(vpath) == 1:
            cherrypy.request.params['name'] = vpath.pop()  # add sections from the url to the request params
            return self.file_expose  # return the method to handle the request
        elif len(vpath) == 2:  # to the same for the post request handler
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
        if name in self.display_functions:
            return self.display_functions[name](*args, **kwargs)  # execute function pass args and kwargs
        elif (name + ".html") in self.files:
            if os.name == 'posix':
                return template.Template.self_render_template("sites/" + name + ".html")
            elif os.name == 'nt':
                return template.Template.self_render_template("sites\\" + name + ".html")
            else:
                pass  # just to run clearly into the raise of the exception
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
        if kwargs['name'] == 'post':
            try:
                return self.postController.execute_function(post_name, args, kwargs)
            except KeyError:
                raise cherrypy.HTTPError(404)
        else:
            raise cherrypy.HTTPError(404)

    def _import_sites(self):
        """
        method for scanning views folder for function files
        :return:
        """
        self.display_functions = dict()  # create empty dict
        if os.name is 'nt':
            filelist = os.listdir(os.getcwd() + "\\view\\")
        elif os.name is 'posix':
            filelist = os.listdir(os.getcwd() + "/view/")
        else:
            filelist = os.listdir(os.getcwd() + os.sep + "model" + os.sep + "request_functions" + os.sep)
        try:
            del filelist[filelist.index("__init__.py")]
            del filelist[filelist.index("__init__.pyc")]  # remove the package init from the list it should'n
            #  have functions to import
        except ValueError:
            # catch exception if python bytecode file is not present
            pass
        for dat in filelist:
            basename, extention = os.path.splitext(dat)  # split the filename and fileextention
            if extention == ".py":  # check if is is a python code file
                try:
                    mod = importlib.import_module("." + basename, "view")  # import module from view
                    if hasattr(mod, "INIT"):  # check if module has INIT variable and it's a Function reference
                        init_func = mod.INIT
                        if callable(init_func):
                            functions = init_func()  # execute the init function
                        elif isinstance(init_func, dict):
                            functions = init_func
                        else:
                            functions = dict()
                        if isinstance(functions, dict):

                            if isinstance(functions, dict):
                                for key, data in functions.iteritems():
                                    if key not in self.display_functions:
                                        self.display_functions[key] = data
                                        print("Imported Display Function " + key)
                                    else:
                                        print("Module " + str(basename) + " can't register function " + key
                                              + " Name already exist")
                except ImportError, e:
                    print("Could not Import " + str(basename) + "\nError message: " + e.message)
                except ValueError:
                    pass
        return


