# sudo pip install boto3 // SDK

import boto3
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

bkt_name = "bkt-wtemp"

def conn_s3():
    try:
        session_aws = boto3.session.Session(ACCESS_KEY, SECRET_KEY)
        s3_resource = session_aws.resource('s3')
        print('\nConnected to S3...\n')
        return s3_resource
    except Exception as e:
        print('Error connecting', e)
        

def img_save(img):
    try:
        # not ext required "/tmp/aws-s3_test.jpg"
        img_path = "/tmp/aws-s3_test"
        img.save(img_path)
        print("Image saved in tmp/\n")
        return img_path
    except Exception as e:
        print('Error', e)
        return False
        
def img_upload(s3conn, img_route, img, iid, fname):
    print("uploading image to S3...\n")
    
    try:
        img_name = img.filename
        print("image name - original:\t", img_name)
        img_ext = img_name.split('.')[-1]
        print("image extension:\t", img_ext)
        img_name_s3 = f"{iid}-{fname}.{img_ext}"
        print("image name - id for s3:\t", img_name_s3, '\n')
        
        # bkt_name = "bkt-wtemp"
        file_dest_name = "upload-test/" + img_name_s3
    
        bkt_conn = s3conn.meta.client.upload_file(img_route, bkt_name, file_dest_name)
    
        print(f"image uploaded as: {img_name_s3}\n")
        return True
    except Exception as e:
        print("error: ", e)
        return False
        
def consult_file(s3conn, iid):
    print("searching...\n")
    
    bkts = s3conn.Bucket(bkt_name)
    bkt_objs = bkts.objects.all()
    
    print('Buckets: ')
    print(bkt_objs)
    print(" ")
    
    for obj in bkt_objs:
        print(obj)
    print(" ")
    
    for obj in bkt_objs:
        print(obj.key)
    print(" ")
    
    print(type(bkt_objs))
    print(" ")
    
    bkt_path_list = []
    
    for obj in bkt_objs:
        #bkt_path_list.append(obj.key)
        file_s3_path = obj.key
        file_s3_name = file_s3_path.split('/')[-1].split('-')[0]
        
        if file_s3_name == iid:
            print('OK... file name s3: ', file_s3_name)
            return file_s3_path

    return None
    #print(bkt_path_list[0])
    #print(" ")
    
    #try:
        
    #except Exception as e: