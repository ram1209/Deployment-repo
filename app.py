from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import security as sec
from resources.item import Item,Itemlist
from resources.user import UserRegister
from resources.store import Store,StoreList
#import user as usr
import sqlite3
from werkzeug.security import safe_str_cmp
app=Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

app.secret_key="jose"
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS']=False
jwt=JWT(app,sec.authenticate,sec.identity)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'

api.add_resource(Item,'/item/<string:name>')
api.add_resource(Itemlist,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')
if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
