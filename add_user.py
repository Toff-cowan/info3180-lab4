"""One-off script to add a user for Exercise 3. Run: python add_user.py"""
from app import app, db
from app.models import UserProfile

with app.app_context():
    user = UserProfile(
        first_name="Test",
        last_name="User",
        username="testuser",
        password="password"
    )
    db.session.add(user)
    db.session.commit()
    print("User added: testuser / password")
