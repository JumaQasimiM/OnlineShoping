# Products file
from datetime import datetime
class Products:
	def __init__(self, name, description, price, category, stock=0):
		self.name = name
		self.description = description
		self.price = price
		self.category = category
		self.stock = stock
		self.created_at = datetime.now()


	# save 
	def save(self):
		pass

