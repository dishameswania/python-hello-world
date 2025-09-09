import sqlite3

# Connect to a SQLite database (it will create one if it doesn't exist)
connection = sqlite3.connect('example.db')

# Create a cursor object using the cursor() method
cursor = connection.cursor()

# Creating a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS greetings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT NOT NULL
)
''')

# Inserting "Hello World" into the table
cursor.execute("INSERT INTO greetings (message) VALUES ('Hello World')")

# Committing the transaction
connection.commit()

# Fetching the "Hello World" message
cursor.execute("SELECT message FROM greetings")
greeting = cursor.fetchone()

# Print the retrieved message
if greeting:
    print(greeting[0])  # Output should be "Hello World"

# Close the cursor and the connection
cursor.close()
connection.close()
