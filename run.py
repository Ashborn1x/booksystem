from app import create_app, db
from flask_migrate import Migrate
from app.models import Author, Genre, Book

app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
