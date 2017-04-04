"""
Main Controller to handle Http Post requests
Version 1.0
"""
import cherrypy
import os
import importlib


class PostController(object):
    """
    Class for holding and controlling function based modules e.g. Post-Requests
    """
    def __init__(self, plugin_path=None):
        """
        Constructor of the PostController Class
        :param plugin_path: Path of the Module Directory
        """
        if isinstance(plugin_path, (str, list)):
            if isinstance(plugin_path, str):
                self.plugin_path = list(plugin_path)  # store it into one list
            else:
                self.plugin_path = plugin_path  # store list in class variable
        self.functions = dict()  # create empty dict
        self._import_modules()  # load modules into the class with names
        return

    def _check_plugin_function(self, plugin_function_name):
        """
        this function will check if given function name is present
        :param plugin_function_name: name of the function
        :return: True if function is known, False otherwise
        """
        if not isinstance(plugin_function_name, str):
            return False
        if plugin_function_name in self.functions:
            return True
        else:
            return False

    def _import_modules(self):
        """
        wrapper function to import all functions founded at request_functions
        :return:
        """
        if os.name is 'nt':
            filelist = os.listdir(os.getcwd() + "\\model\\request_functions\\")
        elif os.name is 'posix':
            filelist = os.listdir(os.getcwd() + "/model/request_functions/")
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
                    mod = importlib.import_module("." + basename, "model.request_functions")  # import module from view
                    if hasattr(mod, "INIT"):  # check if module has INIT variable and it's a Function reference
                        init_func = mod.INIT
                        if callable(init_func):
                            functions = init_func()  # execute the init function
                        elif isinstance(init_func, dict):
                            functions = init_func
                        else:
                            functions = dict()  # create empty dict for avoid exception
                        if isinstance(functions, dict):
                            for key, data in functions.iteritems():
                                if key not in self.functions:
                                    self.functions[key] = data
                                    print("Imported Module Function " + key)
                                else:
                                    print("Module " + str(basename) + " can't register function " + key
                                          + " Name already exist")
                except ImportError, e:
                    print("Could not Import " + str(basename) + "\nError message: " + e.message)
                except ValueError:
                    pass
        return

    def get_function(self, function_name):
        """
        Function searches for function name raises an Exception if not found
        :param function_name: Name of the Function
        :return: Reference to the Function
        """
        if self._check_plugin_function(function_name):
            return self.functions[function_name]
        else:
            raise KeyError()

    def execute_function(self, function_name, *args, **kwargs):
        """
        Search and Execute the function raise Exception if not found

        :param function_name:
        :param args: arguments passed to the function
        :param kwargs: keyword arguments passed to the function
        :return: return values of the Function
        """
        if self._check_plugin_function(function_name):
            return self.functions[function_name](args, kwargs)
        else:
            raise KeyError()

if __name__ == '__main__':
    print("this is a test run")
    cwd = os.getcwd()
    print(cwd)
    if os.name is 'posix':
        cwd = cwd.split('/')
    else:
        cwd = cwd.split('\\')
    cwd.pop()
    cwd.append('model')
    cwd.append('request_functions')
    if os.name is 'posix':
        cwd = str('/').join(cwd)
    else:
        cwd = str('\\').join(cwd)
    print(cwd)
    PostController(cwd)
