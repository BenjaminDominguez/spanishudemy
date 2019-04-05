def create_users():

    from app.models import User
    from app import db

    user1 = User(username="ben")
    user2 = User(username="carlos")

    db.session.add_all([user1, user2])
    db.session.commit()

    