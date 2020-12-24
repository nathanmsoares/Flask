from flask import  render_template, url_for, flash, redirect
from aplicativo import app
from aplicativo.forms import RegistrationForm, LoginForm
from aplicativo.models import User, Post


posts = [
    {
        'author': 'Teste 1',
        'title': 'Titulo teste 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Teste 2',
        'title': 'Titulo teste 2',
        'content': 'second post content',
        'date_posted': 'April 20, 2020(2)'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect('home')
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form =  LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'sucess')
            return redirect(url_for('home'))
        else:
            flash('Login Unsucessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
    