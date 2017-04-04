"""
test file for dynamic load of functions at runtime
"""


def testing(*args, **kwargs):
    return "this is a test function"


def init():
    return {'test': testing}

INIT = init


class my_test_class(object):
    var1 = 0

    def __init__(self):
        pass