from flask import *
from public import public
from admin import admin
from salon import salon
from staff import staff
from api import api

app=Flask(__name__)

app.secret_key="salon"
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(salon)
app.register_blueprint(api,url_prefix='/api')

app.run(debug=False,port=5678,host="0.0.0.0")

