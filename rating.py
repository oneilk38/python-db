from main import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DECIMAL


class Rating(db.Model):
    __tablename__ = "ratings"
    movie_id = Column(Integer, ForeignKey("movies.id"), primary_key=True)
    reviewer_id = Column(Integer, ForeignKey("reviewers.id"), primary_key=True)
    rating = Column(DECIMAL, nullable=False)


def get_ratings():
    ratings = Rating.query.all()
    for rating in ratings:
        print(f'{rating.rating}, {rating.reviewer_id}, {rating.movie_id}')


def seed_ratings():
    rating = Rating(movie_id=3, reviewer_id=10, rating=9.5)
    db.session.add(rating)
    db.session.commit()
