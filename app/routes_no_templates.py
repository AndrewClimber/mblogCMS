# -*- coding: utf-8 -*-

from app import mblog_app

@mblog_app.route('/')
@mblog_app.route('/index')
def index():
    user = {'username': 'miguel'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
