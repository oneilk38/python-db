from main import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DECIMAL


class Reviewer(db.Model):
    __tablename__ = "reviewers"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)


def get_reviewers():
    reviewers = Reviewer.query.all()
    for reviewer in reviewers:
        print(f'{reviewer.first_name}, {reviewer.last_name}')


def seed_reviewers():
    reviewer = Reviewer(first_name="Kevin", last_name="Byrne")
    db.session.add(reviewer)
    db.session.commit()