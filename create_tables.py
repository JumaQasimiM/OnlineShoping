
from databaseconnection import DatabaseConnection

cursor = DatabaseConnection.get_cursor()

# create users table
cursor.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT ,
						username TEXT NOT NULL UNIQUE,
						email TEXT NOT NULL UNIQUE,
						password TEXT NOT NULL,
						-- salt TEXT NOT NULL,
						created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
						  );''')

# create orders table

cursor.execute('''CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY AUTOINCREMENT ,
						user_id INTEGER NOT NULL,
						totle_amount INTEGER NOT NULL,
						status TEXT NOT NULL,
						-- salt TEXT NOT NULL,
						created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
						  );''')


cursor.connection.commit()