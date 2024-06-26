from flask import render_template, request
from database.db import connectionSQL, add_user, consultUserDB
#from database.db import *
from admin.admin_s3 import conn_s3, img_save, img_upload
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
    image = request.files['image']
    
    print(f"\nId: {id}\nName: {name}\nLast name: {last_name}\nDate: {birth_date}\n")
    print(f"Image name: {image.filename}")
    
    res = add_user(id, name, last_name, birth_date)
    
    #print(type(id))
    #print(res)
    
    '''
    connect_s3 = conn_s3()
    image_path = img_save(image)
    image_confirm = img_upload(connect_s3, image_path, image, id)
    '''
    
    if res == True:
        connect_s3 = conn_s3()
        image_path = img_save(image)
        image_confirm = img_upload(connect_s3, image_path, image, id)
        
        if image_confirm:
            return render_template('register.html')
        else:
            return "<h2>image was not saved</h2>"
    else:
        return "<h2>User was not created</h2>"
    
def fconsultPage():
    return render_template('consult.html')

def fconsultUser():
    userObj = request.get_json()
    id = userObj["id"]
    print('\n' + id + '\n')
    res = consultUserDB(id)
    print("res:")
    print(res)
    print("control.py\n")
    
    if res != False and len(res) != 0:
        answ = {
            'status': 'OK...',
            'name': res[0][1]
        }
        print(f"\nName obtained from the db: {answ['name']}\n")
    else:
        answ = {
            'status': 'ERROR...'
        }
        print("User not found")
    return answ