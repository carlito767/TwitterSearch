# Sources:
# https://pythonise.com/series/learning-flask
# https://preslav.me/2019/01/09/dotenv-files-python/

# Settings
from dotenv import load_dotenv
load_dotenv()

from app import app

if __name__ == '__main__':
    app.run()
