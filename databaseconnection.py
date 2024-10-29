
# database connection
import sqlite3

class DatabaseConnection:
	""" Database connection 
	Frist: open the connection
	Second: curser
	Third: Close the Connection
	"""
	_connection = None

	# open connction
	@classmethod
	def open_connection(cls,database_name):
		# open if it colsed
		if cls._connection is None:
			cls._connection = sqlite3.connect(database_name)
			return cls._connection
	
	# close connection
	@classmethod
	def close_connection(cls):
		# close if opend

		if cls._connection is not None:
			cls._connection.close()
			cls._connection = None

	# curser

