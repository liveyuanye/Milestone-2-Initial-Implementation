from app import myapp_obj
from flask import render_template
from flask import redirect
from app.forms import LoginForm
from app.models import User, Post
from app import db
# from <X> import <Y>

@myapp_obj.route("/")
def main():
    name = "Welson"
    return render_template("hello.html", name=name)

@myapp_obj.route("/accounts")
def users():
    return "My USER ACCOUNTS"

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

# A9Q1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    db.create_all()     # Creates database

    if form.validate_on_submit():

        u = User(username=form.username.data, password=form.password.data)
        db.session.add(u)   # 'Staging' process
        db.session.commit() # Saves to database

        print(f"Here is the input from the user {form.username.data} and {form.password.data}")
        return redirect("/")
    else:
        print("MOOOO MOOO")
    return render_template("login.html", form=form)
    # What is render_template returning?
    # return str(type(render_template("login.html", form=form)))

@myapp_obj.route("/usertable")
def usertable():
    users = User.query.all()
    for u in users:
        print(u.id, u.username, u.password, u.email)
    return render_template("usertable.html", Users=users)


# A9Q3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@myapp_obj.route("/posts")
def showall():
    posts = Post.query.all()
    for p in posts:
        print(p.id, p.username, p.body, p.timestamp, p.user_id)
    return render_template("posttable.html", Posts=posts)