import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://default:4T2xWfmzOYgZ@ep-shiny-lake-a4u2wx0x-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require')