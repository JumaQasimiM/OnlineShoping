# Payments file

from datetime import datetime
from databaseconnection import DatabaseConnection
class Payment:
	def __init__(self, order_id, amount, payment_method, status= 'panding'):
		self.order_id = order_id
		self.amount = amount
		self.payment_method = payment_method
		self.status = status
		self.created_at = datetime.now()

	def __repr__(self):
		return  f"order_id = {self.order_id}, amount = {self.amount}, status = {self.status}"

	def save(self):
		# database connention

		curser = DatabaseConnection.get_curser()
		# curser.execute('''INSERT INTO payment (order_id, ...) VALUSE (?, ?, ?,...)''',(self.order_id,...))

		DatabaseConnection._connection.commit()
		pass


