# -*- coding: utf-8 -*-

from flask import Flask
from config import config
from logbook.web.extensions import assets
import javascript


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    assets.init_app(app)
    assets.register('js_all', javascript.js_all)

    from public import public as public_blueprint
    app.register_blueprint(public_blueprint)

    return app
