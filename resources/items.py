
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.items import ItemModel



class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price', type=float, required=True, help= 'Required')
	parser.add_argument('store_id', type=int, required=True, help= 'Required')
		
	@jwt_required()
	def get(self,name):
		item = ItemModel.find_by_name(name)
		if item:
			return item.json()
		return {'message' : 'Item does not exists'}
	
	
	
	
	def post(self,name):
		if ItemModel.find_by_name(name):
			return {'message' : 'Item already exists'}

		data = Item.parser.parse_args()

		item = ItemModel(name, data['price'], data['store_id'])
		
		try: 
			item.savetodb()
		except:
			{'message' : 'An error occured'}
		return item.json()

	def delete(self,name):
		item = ItemModel.find_by_name(name)
		if item:
			item.delete()
		
		return {'message' : 'Item deleted successfully'}		

	def put(self, name):
		
		data = Item.parser.parse_args()
		item = ItemModel.find_by_name(name)
		
		
		if item is None:		
			item = ItemModel(name, data['price'], data['store_id'])
		else:
			item.price = data['price']
		
		item.savetodb()

		return item.json()

	


class Itemlist(Resource):
	def get(self):
		return {'item': [item.json() for item in ItemModel.query.all()]}
