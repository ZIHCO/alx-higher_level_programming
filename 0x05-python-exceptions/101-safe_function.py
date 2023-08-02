#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        return fct(*args)
    except ValueError as err:
        stderr.write("Exception: {}\n".format(err))
        return None
    except TypeError as err:
        stderr.write("Exception: {}\n".format(err))
        return None
    except ZeroDivisionError as err:
        stderr.write("Exception: {}\n".format(err))
        return None
    except IndexError as err:
        stderr.write("Exception: {}\n".format(err))
        return None
