from livereload import Server, shell
from pelican import Pelican
from pelican.settings import read_settings

# the live reload does not seem to work with articles in "draft" status

p = Pelican(read_settings('pelicanconf.py'))

def compile():
    try:
        p.run()
    except SystemExit as e:
        pass

server = Server()
server.watch('content/', compile)
server.serve(root='output', host='localhost', port=8000) # serves website at localhost:8000