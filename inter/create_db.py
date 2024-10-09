import sqlite3

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('votes.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Create the "votes" table
cur.execute('''
    CREATE TABLE IF NOT EXISTS votes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        choice TEXT NOT NULL,
        count INTEGER NOT NULL DEFAULT 0
    )
''')

# Insert initial values for anime and manhwa
cur.execute('INSERT INTO votes (choice, count) VALUES ("anime", 0)')
cur.execute('INSERT INTO votes (choice, count) VALUES ("manhwa", 0)')

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Database setup complete!")
