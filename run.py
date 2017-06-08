""" Version:1.0 """

from __builtin__ import dict

import signal
import os

try:
    import cherrypy
except ImportError, e:
    print "ERROR dependencies not satisfied\nRunning pip to get them"
    import pip
    pip.main(args=["install", "-r", "requirements.txt"])
    import cherrypy

import controller.RootController
from model.template import Template


def shutdown(signum, frame):
    print "try shutdown"
    cherrypy.server.stop()

signal.signal(signal.SIGINT, shutdown)

config = dict()
site_config = dict()
config['log.error_file'] = 'err.log'  # error log file
cherrypy.config.update(config)
config.clear()
conf = {
        '/': {
            'tools.staticdir.root': os.getcwd()

        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'static',


            # we don't need to initialize the database for static files served by CherryPy
            # 'tools.db.on': False
        }
    }
cherrypy.tree.mount(controller.RootController.RootController(), config=conf)
# bind root controller to server root
cherrypy.server.start()
