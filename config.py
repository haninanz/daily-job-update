import os
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv = os.path.join(base_dir, '.env')

SECRET_KEY = os.environ.get('SECRET_KEY')