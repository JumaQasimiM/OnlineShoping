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

	# get user form database
	def get_user_by_id(self, user_id):
		if user_id == -1:
			# not found
			pass
		else:
			# form db take the user 
			pass
	# delete form database
	def remove_user(self, user_id):
		if user_id == -1:
			# not found
			pass
		else:
			# delete
			pass
	@staticmethod
	def get_all_user():
		pass



