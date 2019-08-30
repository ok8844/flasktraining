from models.user import UserModel


def authenticate(username, password):
	user = UserModel.findbyusername(username)
	if user and user.password == password:
		return user

def identity(payload):
	user_id = payload['identity']
	return UserModel.findbyuserid(user_id)




