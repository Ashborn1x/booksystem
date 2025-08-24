from flask import Blueprint, jsonify, request
from .models import Author, Genre, Book
from . import db

main = Blueprint('main', __name__)

# AUTHORS
@main.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    return jsonify([{
        "id": a.id,
        "name": a.name,
        "books": [b.title for b in a.books]
    } for a in authors])

@main.route('/authors/<int:id>', methods=['GET'])
def get_author(id):
    author = Author.query.get_or_404(id)
    return jsonify({
        "author":{
            "id": author.id,
            "name": author.name,
            "books": [b.title for b in author.books]
            }
    }), 200

@main.route('/authors', methods=['POST'])
def post_authors():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    new_author = Author(name=data['name'])
    db.session.add(new_author)
    db.session.commit()
    return jsonify({
        "message": f"Author {new_author.name} created.",
        "author": {"id": new_author.id, "name": new_author.name}
    }), 201

@main.route('/authors/<int:id>', methods=['PUT'])
def update_author(id):
    author = Author.query.get_or_404(id)
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    if 'name' in data:
        author.name = data['name']

    db.session.commit()
    return jsonify({
        "message": f"Author {author.name} updated successfully",
        "author": {"id": author.id, "name": author.name}
    }), 200

@main.route('/authors/<int:id>', methods=['DELETE'])
def delete_author(id):
    author = Author.query.get_or_404(id)
    db.session.delete(author)
    db.session.commit()
    return jsonify({"message": f"Author with ID {id} has been deleted."}), 200


# GENRES
@main.route('/genres', methods=['GET'])
def get_genres():
    genres = Genre.query.all()
    return jsonify([{
        "id": g.id,
        "genre": g.genre,
        "books": [b.title for b in g.books]
    } for g in genres])

@main.route('/genres/<int:id>', methods=['GET'])
def get_genre(id):
    genre = Genre.query.get_or_404(id)
    return jsonify({
        "genre":{
            "id": genre.id,
            "genre": genre.genre,
            "books": [b.title for b in genre.books]
            }
    }), 200

@main.route('/genres', methods=['POST'])
def post_genres():
    data = request.get_json()
    if not data or 'genre' not in data:
        return jsonify({"error": "Genre is required"}), 400

    new_genre = Genre(genre=data['genre'])
    db.session.add(new_genre)
    db.session.commit()
    return jsonify({
        "message": f"Genre {new_genre.genre} created.",
        "genre": {"id": new_genre.id, "genre": new_genre.genre}
    }), 201

@main.route('/genres/<int:id>', methods=['PUT'])
def update_genre(id):
    genre = Genre.query.get_or_404(id)
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    if 'genre' in data:
        genre.genre = data['genre']

    db.session.commit()
    return jsonify({
        "message": f"Genre {genre.genre} updated successfully",
        "genre": {"id": genre.id, "genre": genre.genre}
    }), 200

@main.route('/genres/<int:id>', methods=['DELETE'])
def delete_genre(id):
    genre = Genre.query.get_or_404(id)
    db.session.delete(genre)
    db.session.commit()
    return jsonify({"message": f"Genre with ID {id} has been deleted."}), 200

# BOOKS
@main.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{
        "id": b.id,
        "title": b.title,
        "description": b.description,
        "author": b.author.name if b.author else None,
        "genre": b.genre.genre if b.genre else None
    } for b in books])

@main.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        "book":{
            "id": book.id,
            "title": book.title,
            "description": book.description,
            "author":book.author.name if book.author else None,
            "genre": book.genre.genre if book.genre else None
            }
    }), 200

@main.route('/books', methods=['POST'])
def post_books():
    data = request.get_json()
    if not data or 'title' not in data or 'author_id' not in data:
        return jsonify({"error": "Title and author_id are required"}), 400

    # Validate foreign keys
    author = Author.query.get(data['author_id'])
    if not author:
        return jsonify({"error": "Author not found"}), 404

    genre = None
    if data.get('genre_id'):
        genre = Genre.query.get(data['genre_id'])
        if not genre:
            return jsonify({"error": "Genre not found"}), 404

    new_book = Book(
        title=data['title'],
        description=data.get('description'),
        author_id=author.id,
        genre_id=genre.id if genre else None
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({
        "message": f"Book '{new_book.title}' created.",
        "book": {
            "id": new_book.id,
            "title": new_book.title,
            "description": new_book.description,
            "author": author.name,
            "genre": genre.genre if genre else None
        }
    }), 201

@main.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    if 'title' in data:
        book.title = data['title']
    if 'description' in data:
        book.description = data['description']
    if 'author_id' in data:
        author = Author.query.get(data['author_id'])
        if not author:
            return jsonify({"error": "Author not found"}), 404
        book.author_id = author.id
    if 'genre_id' in data:
        genre = Genre.query.get(data['genre_id'])
        if not genre:
            return jsonify({"error": "Genre not found"}), 404
        book.genre_id = genre.id

    db.session.commit()
    return jsonify({
        "message": f"Book '{book.title}' updated successfully",
        "book": {
            "id": book.id,
            "title": book.title,
            "description": book.description,
            "author": book.author.name if book.author else None,
            "genre": book.genre.genre if book.genre else None
        }
    }), 200

@main.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": f"Book with ID {id} has been deleted."}), 200
