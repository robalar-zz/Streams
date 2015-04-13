import streams
from streams import search

import cherrypy
import os
import webbrowser
import multiprocessing as mp
import btclient

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
        s = search.start_search(inp, 1)
        page = self.build_results('public/results.html', inp, search.search_to_html(s))
        return page

    @cherrypy.expose
    def player(self, movieObject, template):
        #redo
        stream = mp.Process(target=btclient.main, args={movieObject.torrents[0]['magnet_link']})
        stream.start()

        with open(template, 'r') as f:
            HTML = f.read()
        HTML = HTML.format(movieObject.title, )
        return HTML
        

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
