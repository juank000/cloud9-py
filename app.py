# server
# pip install flask
# sudo pip install flask

from flask import Flask
#print(dir(Flask))

#app = Flask(__name__, template_folder = '') # default folder tempalte
app = Flask(__name__, template_folder = 'views')
from routes.route import *

if(__name__ == '__main__'):
    #print('hello backend')
    #host = '127.0.0.1'
    host = '0.0.0.0'
    #port = '3000' not on cloud environments
    #port = '8080'
    port = '80'
    app.run(host, port)