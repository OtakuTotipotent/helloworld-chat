from flask import render_template, Blueprint, request
from .models import User
from . import db

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_item = request.form.get("new_item_name")
        if new_item:
            user = User(name=new_item)
            db.session.add(user)
            db.session.commit()
    names_list = User.query.all()
    return render_template("index.html", list=names_list)
