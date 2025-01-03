# Categories file
from datetime import datetime
from databaseconnection import DatabaseConnection
class Category:
	def __init__(self, name, description, parent_id):
		self.name  =name
		self.description = description
		self.parent_id = parent_id
		self.created_at = datetime.now()

	def __repr__(self):
		return f"Category name: {self.name}, description: {self.description}"
	# save into database
	def save(self):
		cursor = DatabaseConnection.get_cursor()
		cursor.execute('''INSERT INTO categories(name, description, parent_id) VALUES('?,?,?')''',
			(self.name, self.description, self.parent_id))
		DatabaseConnection._connection.commit()

