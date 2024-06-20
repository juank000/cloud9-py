from flask import render_template, request
from database.db import connectionSQL, add_user, consultUserDB
#from database.db import *

def fhome():
    #print("Everything's OK")
    connectionSQL()
    #return render_template('hello.html')
    return render_template('index.html')
    
def fregisterPage():
    return render_template('register.html')

def fregisterUser():
    #id = int(request.form['id'])
    id = request.form['id']
    name = request.form['name']
    last_name = request.form['last_name']
    birth_date = request.form['birth_date']
    
    print(f"\nId: {id}\nName: {name}\nLast name: {last_name}\nDate: {birth_date}\n")
    res = add_user(id, name, last_name, birth_date)
    
    #print(type(id))
    #print(res)
    
    if res == True:
        return render_template('register.html')
    else:
        return "User was not created"
    
def fconsultPage():
    return render_template('consult.html')

def fconsultUser():
    userObj = request.get_json()
    id = userObj["id"]
    print('\n' + id + '\n')
    res = consultUserDB(id)
    msg = ''
    
    if res != False and len(res) != 0:
        msg = {
            'status': 'OK...',
            'name': res[0][1]
        }
    else:
        res = {
            'status': 'ERROR'
        }
    return res