# seed.py

from models import db, connect_db, User, Post, Tag
from app import app

def seed_data():
    """Seed the database with initial data."""

    # Create all tables
    db.create_all()

    # Create sample users
    user1 = User(first_name="John", last_name="Doe")
    user2 = User(first_name="Jane", last_name="Smith")

    db.session.add_all([user1, user2])
    db.session.commit()

    # Create sample tags
    tag1 = Tag(name="Flask")
    tag2 = Tag(name="Python")
    tag3 = Tag(name="SQLAlchemy")

    db.session.add_all([tag1, tag2, tag3])
    db.session.commit()

    # Create sample posts
    post1 = Post(title="First Post", content="Content of the first post", user_id=user1.id, tags=[tag1, tag2])
    post2 = Post(title="Second Post", content="Content of the second post", user_id=user2.id, tags=[tag2, tag3])

    db.session.add_all([post1, post2])
    db.session.commit()

    print("Database seeded successfully!")

if __name__ == "__main__":
    with app.app_context():
        seed_data()
