import sqlite3
from db import db

class UserModel(db.Model):
	__tablename__ = 'users'
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50))
	password = db.Column(db.String(50))

	def __init__(self, username, password):
		self.username = username
		self.password = password


	def savetodb(self):
		db.session.add(self)
		db.session.commit()


	@classmethod
	def findbyusername(cls,username):
		return cls.query.filter_by(username = username).first()

	@classmethod
	def findbyuserid(cls,_id):
		return cls.query.filter_by(id=_id).first()
