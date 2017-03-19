"""
Main Controller to handle Http Post requests
Version 1.0
"""
import cherrypy


class PostController(object):
    def __init__(self, Plugin_path):
        if not isinstance(Plugin_path,(str)):
            return  # return from Function if there is nothing e.g. there can be a raise an exception
        import os
        if isinstance(Plugin_path,str):
            plugin_list = os.listdir(Plugin_path)  # get all files in folder
            if '__init__.py' in plugin_list:
                del plugin_list[plugin_list.index('__init__.py')]  # remove python init file if there is something
            plugins = list()
            for files in plugin_list:
                fd, ext = os.path.splitext(files)
                if ext == '.py':
                    plugins.append(fd)
        elif isinstance(Plugin_path,list):
            for path in Plugin_path:
                pass  # add function here

        self._check_plugins(plugins)

    def _check_plugins(self, Plugin_files):
        """
        this function will check in the given Folders for plugins and add them to the mountpoint
        :param Plugin_files: Python Module list
        :return:
        """
        import importlib
        import sys
        for plugin in Plugin_files:
            try:
                module = __import__('model.request_functions.' + module_name, globals(), locals(), func_names, -1)
                print dir(module)
            except ImportError:
                pass

        modules = hasattr(sys.modules,'test')
        print (sys.modules)




if __name__ == '__main__':
    print("this is a test run")
    import os
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
