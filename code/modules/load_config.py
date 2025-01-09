import os
from dotenv import load_dotenv

def watsonx_conf():
    load_dotenv()
    return {
       "WATSONX_APIKEY" : os.getenv('WATSONX_APIKEY'),
       "WATSONX_REGION" : os.getenv('WATSONX_REGION'),
       "WATSONX_PROJECT_ID" : os.getenv('WATSONX_PROJECT_ID')
    }

def app_conf():
    load_dotenv()
    return {
       "APP_USER" : os.getenv('APP_USER'),
       "APP_PASSWORD" : os.getenv('APP_PASSWORD'),
    }
     
    

