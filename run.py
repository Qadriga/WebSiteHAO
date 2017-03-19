""" Version:1.0 """
import cherrypy
import signal
from model.template import Template
from __builtin__ import dict
import os
import controller.RootController


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
