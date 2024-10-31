# Categories file
from datetime import datetime
class Category:
	def __init__(self, name, description, parent_id):
		self.name  =name
		self.description = description
		self.parent_id = parent_id
		self.created_at = datetime.now()

	def __repr__(self):
		return f"Category name: {self.name}, description: {self.description}"


	


	