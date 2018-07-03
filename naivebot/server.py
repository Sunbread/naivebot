#!/bin/env python3
# -*- coding: utf-8 -*-
'The server'

__author__ = 'Sunbread'

import flask
import telegram
if __name__ == '__main__':
    from config import token as config_token
    from config import domain as config_domain
    from config import max_connections as config_max_connections
else:
    from .config import token as config_token
    from .config import domain as config_domain
    from .config import max_connections as config_max_connections

_app = flask.Flask(__name__)
_bot = telegram.Bot(config_token)
def _entryfunc(update): pass

@_app.route('/<token>', methods=['POST'])
def _launcher(token):
    if token != config_token:
        flask.abort(403)
    json = flask.request.get_json()
    if json == None:
        flask.abort(405)
    update = telegram.Update.de_json(json, _bot)
    _entryfunc(update)
    return 'ok'

def entry(func):
    global _entryfunc
    _entryfunc = func
    return func

_bot.set_webhook(url = 'https://%s/%s' % (config_domain, config_token),
                 max_connections = config_max_connections,
                 allowed_updates = [])

application = _app
if __name__ == '__main__':
    application.run()
