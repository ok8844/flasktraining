import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('username', type=str, required=True, help='Required')
	parser.add_argument('password', type=str, required=True, help='Must')
	
	def post(self):
						
		data = UserRegister.parser.parse_args()	
		if UserModel.findbyusername(data['username']):
			return {'message' : 'Username already exists'}

	
		user = UserModel(**data)
		user.savetodb()

		return {'message': "User created"}
