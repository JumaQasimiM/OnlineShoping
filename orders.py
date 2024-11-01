# Orders filee
from datetime import datetime
from databaseconnection import DatabaseConnection
class Order:
	""" status: pending, completed, cancelled """
	def __init__(self, user_id, totle_amount, status='pending'):
		self.user_id = user_id
		self.totle_amount = totle_amount
		self.status = status
		self.created_at = datetime.now()

	# save method
	def save(self):
		cursor = DatabaseConnection.get_cursor()
		cursor.execute('''INSERT INTO orders(user_id, totle_amount, status)
						  VALUES (?,?,?) ''', (self.user_id, self.totle_amount, self.status))
		cursor.connection.commit()

	#update stutus
	@staticmethod
	def update_status(order_id, new_status):
		# update the order status
		cursor = DatabaseConnection.get_cursor()
		cursor.execute('''UPDATE orders SET status = ? WHERE id =?''',(new_status,order_id))
		DatabaseConnection._connection.commit()

	# get all user's orders 
	@staticmethod
	def get_orders_by_user(user_id):

		cursor = DatabaseConnection.get_cursor()
		cursor.execute('SELECT * FROM orders WHERE user_id = ?',(user_id))
		orders = cursor.fetchall()
		return orders




if __name__ == '__main__':
	new_order = Order(user_id = 1, totle_amount = 3,status = 'pending')
	# new1_order = Order(user_id = 1, totle_amount = 4,status = 'completed')
	new_order.save()


	# # update status
	# Order.update_status(1,'completed')
	# print('Order updated successfully!')
	# # get all orders form one user
	user_orders = Order.get_orders_by_user(1)
	# print('user orders: ', user_orders)