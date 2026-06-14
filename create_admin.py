import sys

from werkzeug.security import generate_password_hash

from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():

    password = input("Enter admin password: ")
    if len(password) < 8:
        print("Error: password must be at least 8 characters")
        sys.exit(1)
    confirm = input("Confirm admin password: ")
    if password != confirm:
        print("Error: passwords do not match")
        sys.exit(1)

    hashed_password = generate_password_hash(password)

    user = User.query.filter_by(
        username="admin"
    ).first()

    if user is None:
        user = User(
            username="admin",
            password=hashed_password,
            is_admin=True
        )

        db.session.add(user)
    else:
        user.password = hashed_password
        user.is_admin = True

    db.session.commit()

    print("Admin created or updated!")