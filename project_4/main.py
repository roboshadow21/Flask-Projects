from flask import Flask, render_template, request, redirect, url_for
from models import db, User
from fields import RegistrationFields
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = b"ff75216441b90b0ba55a7b8e77350b8479e0ea71d50548c6941679ad197a9617"
csrf = CSRFProtect(app)
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login/", methods=["GET", "POST"])
def login():
    form = RegistrationFields()
    if request.method == "POST" and form.validate():
        user = User()
        user.name = request.form['name']
        user.surname = request.form['surname']
        user.email = request.form['email']
        user.password = generate_password_hash(request.form['password'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)