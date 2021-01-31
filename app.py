from flask import Flask 
from .api.payment import app

 
if __name__ == '__main__':
    app.run()