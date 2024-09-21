import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://default:4T2xWfmzOYgZ@ep-shiny-lake-a4u2wx0x-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require')
    
    # 지워도 DB에 입력은 됨, 하지만 flash가 안뜨고 오류 500 발생.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # or another method to set a secret key