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
        print('connecting to S3...')
    except Exception as e:
        print('Error connecting', e)
    