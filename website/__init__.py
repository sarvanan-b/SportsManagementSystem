from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



db=SQLAlchemy()
DB_name="database.db"




def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] ='mysecret'
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'  
    db.init_app(app)
    
    from .views import views
    #from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    #app.register_blueprint(auth,url_prefix='/')

    

    create_database(app)
    return app

def create_database(app):
    if not path.exists('database.db'):
        with app.app_context():
            db.create_all()




