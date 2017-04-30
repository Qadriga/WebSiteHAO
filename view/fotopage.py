import model.template as tempaltelib

import os


class Fotopage:

    def __init__(self):
        self.alben = dict()
        self.__read_filesystem()

    def __read_filesystem(self):
        """
        function checks the file system for folders containing pictures for a Photo gallery 
        gallery is placed into "static/images/gallery"  
        :return: 
        """
        try:
            osdirs = os.listdir(os.getcwdu() + u"/static/images/gallery/")
        except OSError, e:
            print e.message
            print "Make gallery Folder"
            os.makedirs(os.getcwdu() + u"/static/images/gallery/")  # create path if not existing
            osdirs = os.listdir(os.getcwdu() + u"/static/images/gallery/")
        dirs = list()  # create empty list to avoid errors
        for elem in osdirs:
            if os.path.isdir(os.getcwdu() + u"/static/images/gallery/" + elem):  # check if elem in dirs is a folder
                self.__find_pictures(os.getcwdu() + u"/static/images/gallery/" + elem)

    def __find_pictures(self, path):
        """
        :param path: path where pictures should be searched 
        :return: nothing (NONE) 
        """
        files = os.listdir(path)
        folder = list()
        for elem in files:
            extention = os.path.splitext(elem)[1]
            if 'png' in extention or 'jpeg' in extention or 'jpg' in extention:
                folder.append(elem)
        self.alben[os.path.basename(path)] = folder

    def fotoalbum(self, *args, **kwargs):
        """
        displays all available Photo_folders
        :return: 
        """
        if 'album' in kwargs:
            return self.album(kwargs.get('album'))
        temp_vars = dict()
        temp_vars['folders'] = self.alben
        return tempaltelib.Template.self_render_template("sites/fotopage.html", temp_vars)

    def album(self, selected_album):
        temp_vars = dict()
        try:
            temp_vars['images'] = self.alben[selected_album]
            temp_vars['foldername'] = selected_album
        except KeyError, e:
            print e
            import cherrypy
            raise cherrypy.HTTPError(status=404, message="Not Found")
        return tempaltelib.Template.self_render_template("sites/fotopage.html", temp_vars)



fotoclass = Fotopage()
INIT = {'fotopage': fotoclass.fotoalbum}
