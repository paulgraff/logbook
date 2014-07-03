#!/usr/bin/env python
import os
from logbook.web import create_app
from flask.ext.script import Manager
from flask.ext.script.commands import Clean, ShowUrls

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
manager.add_command("clean", Clean())
manager.add_command("urls", ShowUrls())

if __name__ == '__main__':
    manager.run()
