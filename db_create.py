from app import create_app, db
from app.models import Author, Genre, Book

app = create_app()

with app.app_context():
    db.create_all()

    # Sample data
    jk = Author(name="J.K. Rowling")
    grr = Author(name="George R.R. Martin")

    fantasy = Genre(genre="Fantasy")
    scifi = Genre(genre="Science Fiction")

    book1 = Book(title="Harry Potter", description="Wizard adventure", author=jk, genre=fantasy)
    book2 = Book(title="A Game of Thrones", description="Political fantasy", author=grr, genre=fantasy)

    db.session.add_all([jk, grr, fantasy, scifi, book1, book2])
    db.session.commit()

    print("Database created and sample data added!")
