# Products file
from datetime import datetime
from databaseconnection import DatabaseConnection
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
		# save new product in database
		curser = DatabaseConnection.get_cursor()
		curser.execute('''INSERT INTO products (name, description, price, category, stock,created_at) 
						  VALUES (?,?,?,?,?,?)''',(self.name, self.description, self.price, self.category, self.stock))
		DatabaseConnection._connection.commit()


	def get_product_by_id(product_id):
		pass
	def update_stock(product_id, quantity):
		# update product in stock
		pass
 	@saticmethod
	def get_all_product(cls):
		# 'SELECT * FROM products'
		pass


if __name__ == '__main__':
	new_product = Products(name = 'Computer',description = 'cori-7', price = 1200,category='Electronice',stock = 144)
	# save new product
	new_product.save()
	print('Product saved successfully!')

	# select a product by id
	# get_product_by_id() is a static method
	product_data = Products.get_product_by_id(1)

	if product_data:print('Product details: ', product_data)
	else:print('product not found!')
