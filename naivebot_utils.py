#!/bin/env python3
# -*- coding: utf-8 -*-
'The utilities of NaiveBot'

__author__ = 'Sunbread'

def is_command(text, command):
    _text = text.lower()
    _command = command.lower()
    if len(_text) < len(_command) + 1:
        return False
    if _text[0] != '/':
        return False
    if _text[1:len(_command)+1] != _command:
        return False
    if len(_text) > len(_command) + 1:
        if _text[len(_command)+1] != ' ':
            return False
    return True
