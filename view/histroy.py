import model.database as db
import model.template as templatelib
import datetime

class Events(object):
    def __init__(self):
        pass

    def site(self):
        temp_vars = dict()
        temp_vars['dates'] = list()
        dates = db.Database().query(table_name="dates", ordered_by=" d_day desc")  # should return a dict tuple
        for items in dates:  # item is an dict in the tuple
            for key, values in items.iteritems():
                if isinstance(values, str):
                    iso = values.decode("iso-8859-1")
                    items[key] = iso
                    #  items[key] = iso.encode("utf-8")  # convert database string into utf-8 encoded string
                elif isinstance(values, datetime.date):
                    items[key] = values.strftime(u"%d %m %Y")

            temp_vars.get('dates').append(items)
        print temp_vars
        return templatelib.Template.self_render_template("sites/veranstaltungen.html", temp_vars)

module_class = Events()
INIT = {'veranstaltungen':  module_class.site}  # declare it to the server as page

if __name__ == "__main__":
    templatelib.Template.path = "/home/robert/Repos/WebSiteHAO/html"
    print Events().site()
    print datetime.date(2016, 1, 1).strftime(u"%d %m %Y")
