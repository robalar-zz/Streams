import Streams
from Streams import Search

import cherrypy
import os
import webbrowser
import multiprocessing as mp
import btclient

class Interface(object):

	def BuildResults(self, template, term, HTMLTable):
		
		with open(template, 'r') as f:
			HTML = f.read()
		HTML = HTML.format(term, HTMLTable)
		return HTML

	@cherrypy.expose
	def index(self):
		return file('public/index.html')

	@cherrypy.expose
	def search(self, inp):
		search = Search.StartSearch(inp, 1)
		page = self.BuildResults('public/results.html', inp, Search.SearchToHTML(search))
		return page

	@cherrypy.expose
	def movie(self, movieObject, template):
		
		stream = mp.Process(target=btclient.main, args={movieObject.torrents[0]['magnet_link']})
		stream.start()

		with open(template, 'r') as f:
			HTML = f.read()
		HTML = HTML.format(movieObject.title, )
		return HTML
		

def LaunchBrowser(url):
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

	b = mp.Process(target=LaunchBrowser, args=('http://localhost:8080',))
	b.start()
	cherrypy.quickstart(Interface(), '/', conf)
