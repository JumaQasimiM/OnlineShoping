# Reviews file
from datetime import datetime
from databaseconnection import DatabaseConnection
class Review:
	def __init__(self, user_id, product_id, rating, comment=None):

		self.created_at = datetime.now()
		pass

	def __repr__(self):
		return f"user_id = {self.user_id}, product_id = {self.product_id}, rating={self.rating}"

	
	def save(self):
		cursor = DatabaseConnection.get_cursor()
		cursor.execute('''INSERT INTO reviews(user_id, product_id, rating, comment)
						  VALUES (?,?,?,?) ''', (self.user_id, self.product_id, self.rating, self.comment))
		cursor._connection.commit()

	@staticmethod
	def get_all():
		pass

	@staticmethod
	def get_Product_by_id():
		pass