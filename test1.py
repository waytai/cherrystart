# -*- coding: utf-8 -*-
import os
import random
import string
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
import cherrypy

parent_path = os.path.abspath('')
pa_path = os.path.join(parent_path, 'element')
css_path = os.path.join(pa_path,'css')
js_path = os.path.join(pa_path,'js')

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        env = Environment(loader=FileSystemLoader(parent_path))
        tmpl = env.get_template('hao.html')
        return tmpl.render(name=123123)

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator(),config={
        '/css':
        { 
            'tools.staticdir.on':True,
            'tools.staticdir.dir':css_path 
        },

        '/js':
        { 
            'tools.staticdir.on':True,
            'tools.staticdir.dir': js_path
        }
    })
