from random import randint, shuffle

from flask import Flask, render_template

# importy do zadania 6:
from random import shuffle
@app.route("/lotto")
def lotto():
    liczby = list(range(1, 49+1))
    shuffle(liczby)
    return render_template(
        'lotto.html',
        liczby=liczby[:6],
    )