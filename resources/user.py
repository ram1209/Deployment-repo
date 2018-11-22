import sqlite3
from flask_restful import Resource,reqparse
import json
from models.user import UserModel



class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('password',type=str,
                        required=True,
                        help="This field cannot be blank")
    def post(self):
        #print("in the post method")
        #print("Resource is ",Resource)
        print("Args are")

        #print ("details are ",UserRegister.parser.parse_args())
        data=UserRegister.parser.parse_args()
        print("data is ",data)
        if UserModel.find_by_username(data['username']):
            return {"message":"User name already exists"}
        # connection=con = sqlite3.connect('data.db')
        # cursor = con.cursor()
        # query="insert into users values (NULL,?,?)"
        # cursor.execute(query,(data['username'],data['password']))
        # connection.commit()
        # connection.close()
        #user=UserModel(data['username'],data['password'])
        user=UserModel(**data)
        user.save_to_db()

        return {"message":"user Created Successfully"},201
