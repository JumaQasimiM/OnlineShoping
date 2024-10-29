# User file
from datetime import datetime
import bcrypt
from databaseconnection import DatabaseConnection

class User:
	""" User class"""
	roll = 'Admin' # class variable shared by all instances

	def __init__(self, username, password, email):
		# instance variable unique to each instance
		self.username = username  
		self.password = password
		self.email = email
		self.created_at = datetime.now()

	def __repr__(self):
		return f"user : {self.name}, roll : {self.roll}"

	# Hash password
	@staticmethod
	def hash_password(password):
		salt = bcrypt.gensalt()
		hashed_password = bcrypt.hashpw(password.encode('utf-8'),salt)
		return hashed_password

	@staticmethod
	def verify_password(hashed_password, password):
		return bcrypt.checkpw(password.encode('utf-8'),hashed_password)


	@staticmethod
	def get_user_by_username(username):
		curser = DatabaseConnection.get_curser()
		# not complet

	@staticmethod
	def authentication(username, password):
		user_data = User.get_user_by_username(username)
		if user_data:
			sorted_password = user_data[2]
				if User.verify_password(sorted_password, password):
					return user_data
				return None


# create Object
if __name__ =='__main__':
	pass








