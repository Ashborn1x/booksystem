from app import db, Author, Genre, Book

def seed():
    db.create_all()
    a1 = Author(name="J.K. Rowling")
    g1 = Genre(genre="Fantasy")
    b1 = Book(title="Harry Potter", description="Wizard boy story", author=a1, genre=g1)

    db.session.add_all([a1, g1, b1])
    db.session.commit()
    print("Database seeded!")

if __name__ == "__main__":
    seed()
