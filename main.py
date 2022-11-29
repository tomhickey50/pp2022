from flask import Flask, request, current_app, render_template

import pprint

app = Flask(__name__)

my_number = None

@app.route('/', methods=['POST', 'GET'])
def main():
    global my_number 
    if request.method == 'POST':
        my_number = request.form.get('num', None)
    return render_template('home.html', num=my_number)

@app.route('/number')
def number():
    global my_number
    return f'{my_number}' if my_number is not None else '0'
