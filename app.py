from dotenv import load_dotenv
import os
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "researchroots.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to continue.")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    GET  -> just show the signup form.
    POST -> the browser submitted the form; create the account.
    """
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        
        if not name or not email or not password:
            flash("Please fill in all fields.")
            return redirect(url_for("signup"))

        if password != confirm_password:
            flash("Passwords do not match.")
            return redirect(url_for("signup"))

        if len(password) < 6:
            flash("Password must be at least 6 characters long.")
            return redirect(url_for("signup"))

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("An account with that email already exists. Please log in.")
            return redirect(url_for("login"))

        hashed_password = generate_password_hash(password)

        new_user = User(name=name, email=email, password_hash=hashed_password)
        db.session.add(new_user)   # stage the new row
        db.session.commit()        # write it to .db

        flash("Account created successfully! Please sign in.")
        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    GET  -> show the login form.
    POST -> AUTHENTICATE: compare submitted credentials to the database.
    """
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = User.query.filter_by(email=email).first()

    
        if user and check_password_hash(user.password_hash, password):
            session["user_id"] = user.id
            session["user_name"] = user.name
            flash(f"Welcome back, {user.name}!")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid email or password.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/dashboard")
@login_required   
def dashboard():
    return render_template("dashboard.html", user_name=session.get("user_name"))


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)