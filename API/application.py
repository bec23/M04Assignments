from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.app_context()

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db=SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    book_name = db.Column(db.String(120), nullable=False) 
    author = db.Column(db.String(120), nullable=False) 
    publisher = db.Column(db.String(120), nullable=False) 
    
    def __repr__(self): 
        return { 
            'id': self.id, 
            'book_name': self.book_name, 
            'author': self.author, 
            'publisher': self.publisher 
            }
    
@app.route('/Books')
def get_books():
    books=Book.query.all()