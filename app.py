# server
# pip install flask

from flask import Flask, render_template, request
#print(dir(Flask))

#app = Flask(__name__, template_folder = '') # default folder tempalte
app = Flask(__name__, template_folder = 'views')

@app.route('/')
def home():
    #print("Everything's OK")
    #return render_template('hello.html')
    return render_template('index.html')
    
@app.route('/register_page') # index.js file function
def registerPage():
    return render_template('register.html')

@app.route('/register_user', methods=['post']) # action register.html form
def registerUser():
    id = request.form['id']
    name = request.form['name']
    last_name = request.form['last_name']
    date = request.form['date']
    print(f"\nId: {id}\nName: {name}\nLast name: {last_name}\nDate: {date}\n")
    #print('\n' + id + ' | ' + name + ' | ' + last_name + ' | ' + date + '\n')
    return render_template('register.html')
  
if(__name__ == '__main__'):
    #print('hello backend')
    host = '127.0.0.1'
    #port = '3000' not on cloud environments
    port = '8080'
    app.run(host, port)