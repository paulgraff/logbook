# -*- coding: utf-8 -*-

from flask import request, render_template

def register(public):

    @public.route('/')
    def main():
        return render_template('main/index.html')
