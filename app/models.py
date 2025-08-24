from . import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    books = db.relationship('Book', backref='author', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Author {self.name}>"

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(80), unique=True, nullable=False)
    books = db.relationship('Book', backref='genre', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Genre {self.genre}>"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=True)

    def __repr__(self):
        return f"<Book {self.title}>"
