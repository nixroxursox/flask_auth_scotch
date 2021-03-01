# main.py

from flask import Blueprint, render_template

from flask_login import login_required, current_user
import logging

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(
    filename="demo.log",
    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)
