# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 22:09:52 2017

@author: onomatopeia
"""

import bottle
import os
from datetime import date

@bottle.route('/static/<directory>/<filename>')
def server_static(directory, filename):
    root = os.path.join(os.getcwd(), 'static', directory)
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
    import lorem
    import random 
    
    posts = []
    today = date.today().toordinal()    
    for i in range(10):
        paragraph = lorem.text()
        post_date = date.fromordinal(random.randint(0, today))
        title = lorem.sentence()
        post_dict = {'post': paragraph, 'date' : post_date, 'author': 'agata', 'title': title}
        posts.append(post_dict)
    posts = sorted(posts, key=lambda post : post['date'])
    return bottle.template('blog2', posts=posts, page='blog')
    
@bottle.get('/post')
def new_entry():
    
    return bottle.template('post', page='post')
    
@bottle.post('/blog')
def add_entry():
    title = bottle.request.forms.get('title')
    author = bottle.request.forms.get('author')
    content = bottle.request.forms.get('content')
    post_date = date.today()
    print('Post "{}"\n by {} added on {}\nContent: {}'.format(title, author, post_date, content))
    return blog()
    
    

bottle.debug(True)
bottle.run(host='localhost', port=8086)  # Start the webserver running and wait for requests
