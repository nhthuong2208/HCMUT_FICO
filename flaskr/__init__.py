from flask import Flask
from .config import *
from .models import *
from .routes import main
from .views import view
app = Flask(__name__)
app.config.from_object(ConfigClass)

# Create database
with app.app_context():
    db.init_app(app)
    db.create_all()

app.register_blueprint(view, url_prefix='/view')
app.register_blueprint(main, url_prefix='/')
