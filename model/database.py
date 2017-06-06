# import _mysql
import MySQLdb as _mysql
from MySQLdb.cursors import DictCursor
MYSQL = True
MYSQL_Database_name = "website"
MYSQL_Database_pw = "password"
MYSQL_Database_usr = "webuser"


class Database(object):
    def __init__(self):
        if MYSQL is False:
            self.con = _mysql.connect("database.db")
        else:
            self.con = _mysql.connect(db=MYSQL_Database_name, user=MYSQL_Database_usr, passwd=MYSQL_Database_pw,
                                      host="127.0.0.1")

    def __del__(self):
        self.con.close()

    def query(self, column=list(), row_selection=dict(), table_name=str(), ordered_by=None):
        """
        Used for to query the database 
        :param column: column names which should be selected
        :param row_selection: selection of an row equal to WHERE statement dict key='value' 
        :param table_name: name of the table which should be used
        :param ordered_by: should be a string with additional arguments for ordering the result
        :return: dict of results
        """
        # SELECT columns FROM table_name WHERE row_selection
        queryargs = list()
        querystring = "SELECT "
        for item in column[:-1]:
            querystring += " %s,"
            queryargs.append(item)
        querystring += "%s FROM " + table_name
        if len(row_selection) != 0:
            querystring += " WHERE "  # make last column and FROM and WHERE statement
        if len(column) == 0:
            column.append("*")
        queryargs.append(column[-1])  # append last item from column
        for key, value in row_selection.iteritems():
            tmp = str(key) + "='" + str(value) + "' "
            querystring += tmp

        if isinstance(ordered_by, str):
            querystring = querystring + " ORDER BY " + ordered_by

        cur = self.con.cursor(DictCursor)  # use the python dict cursor
        print (querystring % tuple(queryargs))

        cur.execute(str(querystring % tuple(queryargs)))

        res = cur.fetchall()
        # print res
        return res


if __name__ == "__main__":
    database = Database()
    database.query(table_name="dates", ordered_by="d_day desc")
