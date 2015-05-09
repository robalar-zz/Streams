"""LEGACY"""

import streams
from streams.search import search

import cherrypy
import os
import webbrowser
import multiprocessing as mp
from streams.streamer import btclient

class Interface(object):

    def build_results(self, template, term, HTMLTable):
        
        with open(template, 'r') as f:
            HTML = f.read()
        HTML = HTML.format(term, HTMLTable)
        return HTML

    @cherrypy.expose
    def index(self):
        return file('public/index.html')

    @cherrypy.expose
    def search(self, inp):
        s = search.start_search(inp)
        page = self.build_results('public/results.html', inp, 
                                  s.html_table)
        return page

    @cherrypy.expose
    def player(self, title, magnet_link):

        btclient.main([magnet_link, '--http', '--debug-log', 'bt-log.txt'])

        raise cherrypy.HTTPRedirect('http://localhost:5001/Submarine%20(2010)/Submarine.2010.720p.BrRip.x264YIFY.mp4')
        

def launch_browser(url):
    webbrowser.open_new_tab(url)

def Init():
    conf = {
         '/': {
             'tools.sessions.on': True,
             'tools.staticdir.root': os.path.abspath(os.getcwd())
         },
         '/static': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': './public'
         },
         '/favicon.ico':
         {
            
         }
    }

    b = mp.Process(target=launch_browser, args=('http://localhost:8080',))
    b.start()
    cherrypy.quickstart(Interface(), '/', conf)
