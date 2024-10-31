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





'''
Parent_id:
1:Book
2:electornik
3:...

'''
new category = Category('Book', 'Electronik book',1)



	