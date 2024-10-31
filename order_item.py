from datetime import datetime

class Order_item:
	"""
	the product price 
	"""
	def __init__(self, order_id, product_id, quantity, price):
		self.order_id = order_id
		self.product_id = product_id
		self.quantity = quantity
		self.price = price
	def __repr__(self):
		return f"quantity : {self.quantity}, Price: {self.price}"
