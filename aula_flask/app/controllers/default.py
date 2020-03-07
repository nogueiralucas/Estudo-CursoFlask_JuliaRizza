from app import app, db
from flask import render_template

from app.models.forms import LoginForm
from app.models.tables import User


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)

    return render_template('login.html', form=form)


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    # Create user
    '''
    i = User("lambdax", "metal-x", "lucasx", "lucas.lambdax.101@gmail.com")
    db.session.add(i)
    db.session.commit()
    return 'Ok'
    '''

    # Read user
    '''
    r = User.query.filter_by(username='lambdax').first()
    print(r.name)
    return 'Ok'
    '''

    # Update user
    r = User.query.filter_by(username='lambdax').first()
    r.name = 'lucas nogueira'
    db.session.add(r)
    db.session.commit()
    return 'Ok'

    # Delete user
    r = User.query.filter_by(username='lambdax').first()
    db.session.delete(r)
    db.session.commit()
    return 'Ok'