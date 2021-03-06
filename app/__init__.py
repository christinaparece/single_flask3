from flask import Flask
from config import Config
from flask_login import LoginManager #for logging users in and maintaining a session
from flask_sqlalchemy import SQLAlchemy #this talk to our database for us
from flask_migrate import Migrate #Makes altering the Database a lot easier

login = LoginManager()

login.login_view = 'auth.login'
login.login_message = "You must be logged in to view the page"
login.login_message_category = "warning"

db = SQLAlchemy()

migrate = Migrate()

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)
    login.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from .blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    
    return app