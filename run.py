""" Version:1.0 """
import cherrypy
import signal

from __builtin__ import dict

import controller.RootController


def shutdown(signum, frame):
    print "try shutdown"
    cherrypy.server.stop()

signal.signal(signal.SIGINT, shutdown)

config = dict()
config['log.error_file'] = 'err.log'  # error log file

cherrypy.config.update(config)
cherrypy.tree.mount(controller.RootController.RootController())  # bind root controller to server root
cherrypy.server.start()
