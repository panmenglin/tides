# -*- coding: utf-8 -*-

def is_fundcode(message):
    try:
        int(message)
        if len(message) == 6:
            return True
        else:
            return False
    except ValueError:
        return False

