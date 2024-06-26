# sudo pip install boto3 // SDK

import boto3
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

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
        img_path = "/tmp/aws-s3_test.png"
        img.save(img_path)
        print("Image saved in tmp/\n")
        return img_path
    except Exception as e:
        print('Error', e)
        return False
        
def img_upload(s3conn, img_route, img, iid):
    print("\nuploading image...\n")
    
    try:
        img_name = img.filename
        print("image name - original:\t", img_name)
        img_ext = img_name.split('.')[1]
        print("image extension:\t", img_ext)
        img_name_s3 = iid +"."+ img_ext
        print("image name - id for s3:\t", img_name_s3, '\n')
        
        bkt_name = "bkt-wtemp"
        file_dest_name = "upload-test/" + img_name_s3
    
        bkt_conn = s3conn.meta.client.upload_file(img_route, bkt_name, file_dest_name)
    
        print(f"image uploaded as: {img_name_s3}\n")
        return True
    except Exception as e:
        print("error: ", e)
        return False