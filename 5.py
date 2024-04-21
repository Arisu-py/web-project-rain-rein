from flask import Flask
from flask import request, render_template, redirect
from flask import url_for

app = Flask(__name__)
s = ''
d = []


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
