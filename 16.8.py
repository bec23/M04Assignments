# assignment 16.8
# Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 16.4. As in 16.6, select and print the title column from the book table in alphabetical order.

import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE books (
    title TEXT,
    author TEXT,
    year INTEGER
)
''')

conn.commit()
conn.close()

from sqlalchemy import create_engine, MetaData, Table, select

engine = create_engine('sqlite:///books.db')

connection = engine.connect()

metadata = MetaData()
metadata.reflect(bind=engine)

books_table = metadata.tables['books']

stmt = select(books_table.c.title).order_by(books_table.c.title)

results = connection.execute(stmt).fetchall()

for row in results:
    print(row.title)

connection.close()
