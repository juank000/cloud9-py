from controller.control import *
from app import app

@app.route('/')
def home():
    return fhome()
    
@app.route('/register_page') # index.js file function
def registerPage():
    return fregisterPage()

@app.route('/register_user', methods=['post']) # action register.html form
def registerUser():
    return fregisterUser()
    
@app.route('/consult_page')
def consultPage():
    return fconsultPage()

@app.route('/consult_user', methods=['post'])
def consultUser():
    return fconsultUser()