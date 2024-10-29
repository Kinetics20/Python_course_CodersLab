from random import randint, shuffle

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Witaj użytkowniku!"


@app.route("/hello/<imie>")
def hello_somebody(imie):
    return f"Witaj {imie}, miło cię poznać!"


# import do zad_2
import datetime


@app.route("/czas")
def czas():
    return datetime.datetime.now().strftime("%H:%M")


# import do zad_3

@app.route("/czas_act")
def czas_act():
    return datetime.datetime.today().strftime("%Y.%m.%d")


# import do zad_4

@app.route("/licz/<int:liczba1>/<int:liczba2>")
def licz(liczba1, liczba2):
    return str(liczba1 + liczba2)


# import do zad_5
@app.route("/losuj")
def losuj():
    a = randint(0, 100)
    b = randint(100, 999)
    c = randint(1000, 10000)
    return f"number_1 is : {a},<br> number_2 is : {b},<br> number_3 is : {c}"


# import do zad_6
@app.route("/lotto")
def lotto():
    empty_list = []
    for index in range(1, 50):
        empty_list.append(index)

    shuffle(empty_list)
    return render_template(
        'lotto.html',
        l1=empty_list[0], l2=empty_list[1], l3=empty_list[2],
        l4=empty_list[3], l5=empty_list[4], l6=empty_list[5],
    )

    # return str(empty_list[0:6])
    # return ", ".join([str(liczba) for liczba in empty_list[:6]])


# import do zad_6_0

@app.route("/lotek")
def lotek():
    empty_list = []
    for index in range(1, 50):
        empty_list.append(index)

    shuffle(empty_list)
    # return render_template(
    #     'lotto.html',
    #     l1=empty_list[0], l2=empty_list[1], l3=empty_list[2],
    #     l4=empty_list[3], l5=empty_list[4], l6=empty_list[5],
    # )

    # return str(empty_list[0:6])
    return ", ".join([str(liczba) for liczba in empty_list[:6]])


@app.route("/witaj", methods=['GET', 'POST'])
def witaj():
    if request.method == 'GET':
        return render_template('hello.html')
    else:  # POST - odbieramy formularz
        imie = request.form['imie']
        return f'Witaj {imie}!'


@app.route('/kalkulator', methods=['GET', 'POST'])
def kalkulator():
    if request.method == 'GET':
        return render_template('calc_.html')
    else:
        a = int(request.form['a'])
        b = int(request.form['b'])
        if request.form['op'] == '+':
            return str(a + b)
        if request.form['op'] == '-':
            return str(a - b)
        if request.form['op'] == '*':
            return str(a * b)
        if request.form['op'] == '/':
            return str(a / b)


number = randint(1, 100)


@app.route('/guess', methods=['GET', 'POST'])
def guess():
    if request.method == 'GET':
        return render_template('guess.html')
    else:
        user_number = int(request.form['user_number'])
        if user_number < number:
            outcome = 'Za mało'
        elif user_number > number:
            outcome = 'Za dużo'
        else:
            outcome = 'Gratulacje!'
        return render_template('guess.html', outcome=outcome)
        # Gdzieś w szablonie musi być: {{ outcome }}


@app.route('/c-to-f', methods=['GET', 'POST'])
def c_to_f():
    if request.method == 'GET':
        return render_template('konwerter.html')
    else:
        degrees_c = float(request.form['degrees'])
        degrees_f = 9 / 5 * degrees_c + 32
        return str(degrees_f) + '*F'

@app.route('/f-to-c', methods=['GET', 'POST'])
def f_to_c():
    if request.method == 'GET':
        return render_template('konwerter.html')
    else:
        degrees_f = float(request.form['degrees'])
        degrees_c = (degrees_f - 32) * 5 / 9
        return str(degrees_c) + '*C'

if __name__ == "__main__":
    app.run(debug=True)
