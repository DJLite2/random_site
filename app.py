from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "yashirin_kalit"   # session ishlashi uchun kerak

@app.route('/', methods=['GET', 'POST'])
def index():
    number = None

    if request.method == 'POST':
        # foydalanuvchi yangi oraliq kiritgan bo'lsa
        start = int(request.form.get('start'))
        end = int(request.form.get('end'))
        # sessionda saqlaymiz
        session['start'] = start
        session['end'] = end
        number = random.randint(start, end)

    elif 'start' in session and 'end' in session:
        # eski oraliq sessionda bor bo'lsa
        start = session['start']
        end = session['end']
        number = random.randint(start, end)

    return render_template("index.html", number=number, start=session.get('start'), end=session.get('end'))

if __name__ == "__main__":
    app.run(debug=True)