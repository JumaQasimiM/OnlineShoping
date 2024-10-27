# Reviews file
from datetime import datetime

class Review:
	def __init__(self, user_id, product_id, rating, comment=None):

		self.created_at = datetime.now()
		pass

	def __repr__(self):
		return f"user_id = {self.user_id}, product_id = {self.product_id}, rating={self.rating}"

	# database connection hier
	def database_connection(self):
		pass

	def save(self):
		pass

	@staticmethod
	def get_all():
		pass

	def get_Product_by_id():
		pass