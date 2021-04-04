# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db
import logging
import auxiliary

logEngine = logging.getLogger(__name__)
print(logEngine)
logEngine.basicConfig(
    level="DEBUG",
    filename="demo.log",
    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    name = request.form.get("name")
    password = request.form.get("password")
    user = User.query.filter_by(name=name).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if (
        not user
        or not nacl.pwhash.argon2id.str.verify(user.password, b"password")
        or not nacl.pwhash.argon2id.str.verify(user.PIN, b"PIN")
    ):
        flash("Please check your login details and try again.")
        return redirect(url_for("auth.login"))
    login_user(user, remember=remember)
    return redirect(url_for("main.profile"))


@auth.route("/signup")
def signup():
    return render_template("signup.html")


@auth.route("/signup", methods=["POST"])
def signup_post():
    name = request.form.get("name")
    password = request.form.get("password")
    PIN = request.form.get("PIN")
    user = User.query.filter_by(
        name=name
    ).first()  # if this returns a user, then the email already exists in database

    if (
        user
    ):  # if a user is found, we want to redirect back to signup page so user can try again
        flash("Email address alrejfpady exists")
        return redirect(url_for("auth.signup"))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(
        name=name,
        password=nacl.pwhash.argon2id.str(b"password"),
        PIN=nacl.pwhash.argon2id.str(b"PIN"),
    )

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.login"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
