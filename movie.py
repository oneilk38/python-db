from main import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DECIMAL


class Movie(db.Model):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String, nullable=False)
    release_year = Column(Integer, nullable=False)
    genre = Column(String, nullable=False)
    collection_in_mil = Column(Integer, nullable=False)


def get_movies():
    movies = Movie.query.all()
    for movie in movies:
        print(f'{movie.title}, {movie.release_year}')


def seed_movies():
    movie = Movie(title="Departed", release_year=2006, genre="Drama", collection_in_mil=2)
    db.session.add(movie)
    db.session.commit()