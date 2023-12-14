# На Flask cоздать страницу, на которой будет форма для ввода имени и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

import secrets
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

app.secret_key = bytes(secrets.token_hex(16), encoding='utf-8')

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('form'))
    return render_template('forms/flash.html')

if __name__ == '__main__':
    app.run(debug=True)
