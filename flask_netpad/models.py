# Flask-Netpad
# version 1.0-alpha
# (C) Abstergo 2018
## models.py

# Imports
import datetime
from flask_mongoengine import MongoEngine
from flask_netpad.app import app

# Declares
db = MongoEngine()
db.init_app(app)


# Note Model
class Note(db.DynamicDocument):
    created = db.DateTimeField(default=datetime.datetime.now(), require=True)
    slug = db.StringField(unique=True, require=True)
    title = db.StringField(max_length=60)
    author = db.StringField(max_length=60, require=True)
    content = db.StringField()
    deleted = db.BooleanField(default=False)
    fat = db.DictField()
