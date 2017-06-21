# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 22:09:52 2017

@author: onomatopeia
"""

import bottle
import os
from datetime import datetime
import time

@bottle.route('/static/<directory>/<filename>')
def server_static(directory, filename):
    base_dir = os.path.dirname(__file__)
    root = os.path.join(base_dir, 'static', directory)
    print(root)
    return bottle.static_file(filename, root=root)
    
@bottle.route('/')
def index():
    return bottle.template('index', page='index')
    
@bottle.route('/about')
def about():
    return bottle.template('about', page='about')
    
@bottle.get('/blog')
def blog():
    from dao import DataAccessObject
    with DataAccessObject() as data_access_object:
        posts = data_access_object.select()
    return bottle.template('blog2', posts=posts, page='blog')
    
@bottle.get('/post')
def new_entry():
    return bottle.template('post', page='post')
    
@bottle.post('/blog')
def add_entry():
    data = dict()
    data['TITLE'] = bottle.request.forms.get('title')
    data['AUTHOR'] = bottle.request.forms.get('author')
    data['CONTENT'] = bottle.request.forms.get('content')
    data['POST_DATE'] = datetime.fromtimestamp(time.time())
    from dao import DataAccessObject
    with DataAccessObject() as data_access_object:
        data_access_object.insert(data)
    return blog()
    
application = bottle.default_app()
# application.run()


