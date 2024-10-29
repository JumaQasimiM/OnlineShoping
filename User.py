# User file
class User:
	""" User class"""
	roll = 'Admin' # class variable shared by all instances
	def __init__(self, name, password, roll):
		# instance variable unique to each instance
		self.name = name  
		self.password = password
		self.roll = roll

	def __repr__(self):
		return f"user : {self.name}, roll : {self.roll}"

	def get_user_by_id(self, user_id):
		if user_id == -1:
			# not found
			pass
		else:
			# form db take the user 
			pass

	def remove_user(self, user_id):
		if user_id is not None:
			# found
			# SELECT FROM TABLE user ...
			print('user found')


	@staticmethod
	def get_all_user():
		pass


# create Object
if __name__ =='__main__':
	u = User('juma','jksdhf','Admin')
	u.get_user_by_id(241234)

	# static method
	User.get_all_user()












