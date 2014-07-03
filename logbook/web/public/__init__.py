# -*- coding: utf-8 -*-

from flask import Blueprint

public = Blueprint('public', __name__)

from .main import register as register_main

register_main(public)
