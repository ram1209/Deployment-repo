import sqlite3
from db import db
class UserModel(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80))
    password=db.Column(db.String(80))

    def __init__(self,username,password):
        #self.id=_id
        self.username=username
        self.password=password
        self.something="hi"
    @classmethod
    def find_by_username(cls,username):

        # con=sqlite3.connect('data.db')
        # #print("in to the user method",)
        # cursor=con.cursor()
        # query='select * from users where username=?'
        # result=cursor.execute(query,(username,))
        # row=result.fetchone()#first row
        # print("row is ",row)
        # if row:
        #     #user=cls(row[0],row[1],row[2])
        #     user=cls(*row)
        # else:
        #     user=None
        # cursor.close()
        # con.close()

        return cls.query.filter_by(username=username).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls,_id):
        # con = sqlite3.connect('data.db')
        # cursor = con.cursor()
        # query = 'select * from users where id=?'
        # result = cursor.execute(query, (_id,))
        # row = result.fetchone()  # first row
        # print("row is ", row)
        # if row:
        #     # user=cls(row[0],row[1],row[2])
        #     user = cls(*row)
        # else:
        #     user=None
        # cursor.close()
        # con.close()
        # print("user is ",user)

        return cls.query.filter_by(id=_id).first()
