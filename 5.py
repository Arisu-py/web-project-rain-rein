from flask import Flask
from flask import request, render_template, redirect, session
from flask import url_for
from data import db_session, fan_api
from data.fan import Fan
from data.users import User
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
s = ''
d = []
DB_NAME = 'rain'


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    global d
    d = []
    if request.method == 'GET':
        return render_template("edit.html", title="title")
    elif request.method == 'POST':
        s = request.form['about']
        s = s.replace("<", "(")
        s = s.replace(">", ")")
        for i in s:
            d.append(i)
        d = "".join(d)
        d = d.split("\n")
        with open('text.txt', "w", encoding="UTF-8") as e:
            e.write(s)
        print(d)

        return redirect("/home")


@app.route('/book')
def book():
    return render_template("book.html", text=d)


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/enter')
def enter():
    return render_template("enter.html")


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.name == form.name.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            password=form.password.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(Fan)
    return render_template("index.html", news=news)


def main():
    db_session.global_init(f"db/{DB_NAME}.db")
    #user = User()
    #user.name = "Пользователь 2"
    #user.password = "qwerty123"
    #user.about = 'hi everyone'
    #db_sess = db_session.create_session()
    #db_sess.add(user)
    #db_sess.commit()
    #fill_users(DB_NAME)
    app.register_blueprint(fan_api.blueprint)
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
