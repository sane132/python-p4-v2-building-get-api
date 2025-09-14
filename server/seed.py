# server/seed.py
from app import app
from models import db, Game, Review, User

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Create sample games
    game1 = Game(title="Mega Adventure", genre="Survival", platform="XBox", price=30)
    game2 = Game(title="Golf Pro IV", genre="Sports", platform="PlayStation", price=20)
    game3 = Game(title="Dance, dance, dance", genre="Party", platform="PlayStation", price=7)
    
    # Create sample users
    user1 = User(name="Jose Coleman")
    user2 = User(name="Joshua Brown")
    user3 = User(name="Emily Chen")
    
    # Create sample reviews
    review1 = Review(score=9, comment="Amazing action", game=game1, user=user1)
    review2 = Review(score=5, comment="Not enough levels", game=game1, user=user2)
    review3 = Review(score=8, comment="Great graphics", game=game2, user=user1)
    review4 = Review(score=7, comment="Fun with friends", game=game3, user=user3)
    
    # Add all to session and commit
    db.session.add_all([game1, game2, game3, user1, user2, user3, review1, review2, review3, review4])
    db.session.commit()
    
    print("Database seeded successfully!")