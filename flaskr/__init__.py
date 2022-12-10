from flask import Flask
from .config import *
from .models import *
from .routes import main

app = Flask(__name__)
app.config.from_object(ConfigClass)

# Create database
with app.app_context():
    db.init_app(app) 
    db.create_all()

    if len(BankData.query.all()) < 100:
        data_set = read_dataset()
        data = []
        for index in range(len(data_set) - 90):
            row = {}
            for col in COL_NAMES:
                row[col] = data_set.loc[index][col]
                data.append(row)

        for row in data:
            new_line = BankData(row)
            db.session.add(new_line)
            db.session.commit()

app.register_blueprint(main, url_prefix='/')