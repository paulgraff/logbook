# -*- coding: utf-8 -*-

from flask.ext.assets import Bundle

js_all = Bundle(
        'js/jquery-2.1.1.min.js',
        'js/angular.min.js'
        'js/underscore-min.js',
        output='cache/global.js'
    )
