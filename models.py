from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """
    This class represents the 'user' table in researchroots.db.
    Every attribute below becomes a COLUMN in that table.
    Every time we create a User(...) object and save it, it becomes
    a ROW in that table.
    """

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(150), unique=True, nullable=False)

    password_hash = db.Column(db.String(300), nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f"<User {self.email}>"
