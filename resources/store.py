from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
	def get(self,name):
		store = StoreModel.find_by_name(name)
		if store:		
			return store.json()
		
		return {'message' :'Store not available'}

	def post(self, name):
		if StoreModel.find_by_name(name):
			return {'message' : 'Already exists'}
		
		store = StoreModel(name)
		store.savetodb()


	def delete(self,name):
		store = StoreModel.find_by_name(name)
		if store:		 
			store.delete()
		
		return {'message' : 'Deleted'}


class StoreList(Resource): 
	def get(self):
		return {'stores' : [x.json() for x in StoreModel.query.all()]}
