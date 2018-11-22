from flask_jwt import JWT,jwt_required
from flask_restful import Resource,reqparse
import sqlite3
from db import db
from models.item import ItemModel
class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("price",type=float,
                        required=True,
                        help="This field cannot be left blank")
    #parser=reqparse.RequestParser()
    parser.add_argument("store_id",type=int,
                        required=True,
                        help="Every item needs store id")

    @jwt_required()
    def get(self,name):
        # #for item in items:
        #     #print("name is",name)
        #  #   if item['name'] == name:
        #   #      return item
        # item=next(filter(lambda x:x['name']==name,items),None)
        # #next is used for finding a first occurence
        # #if we want to find out another we have to use another next
        # #return {'item':'item not found'},404
        # #return {'student':name}
        # return {'item':item} ,200 if item else 404
        item=ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'item not found'},404




    def post(self,name):
        #item={'name':name,'price':12.00}
        #items.append(item)
        #return item,201
        #print(name)
        if ItemModel.find_by_name(name):
            #print()
        #if next(filter(lambda x:x['name']==name,items),None):
            return {'message':"An item with {} already exists".format(name)},400
        #data=request.get_json()

        data = Item.parser.parse_args()

        print("the data is ",data)

        #item=ItemModel(name,data['price'],data['store_id'])
        item=ItemModel(name,**data)
        try:
            item.save_to_db()
        except:
            return {'message':"Got an error in insertion"},500
        #items.append(item)

        return item.json(),201




        #return item,201
    def delete(self,name):
        # global items
        # item=list(filter(lambda x:x['name']!=name,items))
        # items.append(item)
        # return {"message":"item Deleted"}
        # connection=sqlite3.connect('data.db')
        # cursor=connection.cursor()
        # query='Delete from items  where name=?'
        # cursor.execute(query,(name,))
        # connection.commit()
        # connection.close()
        # return {'message':'Item Deleted'}
        item=ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message":"item deleted"}



    def put(self,name):
        data=Item.parser.parse_args()
        item=ItemModel.find_by_name(name)
        #updated_item=ItemModel{name,data['price']}

        if item is None:
            try:
                item=ItemModel(name,data['price'],data['store_id'])
            except:
                return{"message":"An error occurred in insertion"}
        else:
            try:
                item.price=data['price']
                item.store_id=data['store_id']
            except:
                return {"message": "An error occurred in Updation"}
        item.save_to_db()
        return item.json()




class Itemlist(Resource):
    def get(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = 'select * from items'
        # result=cursor.execute(query, )
        # items=[]
        # for row in result:
        #     items.append({'name':row[0],'price':row[1]})
        #
        #
        # connection.commit()
        # connection.close()
        return {'items':[x.json() for x in ItemModel.query.all()]}
        #return {'items':list(map(lambda x:x.json(),Itemlist.query.all()))}
        #return {'items':items}
