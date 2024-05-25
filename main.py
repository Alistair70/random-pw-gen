from flask import Flask,render_template,request, redirect, url_for, make_response, session, jsonify

import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gen_password', methods=['POST','GET'])
def gen_password():
    length = request.json.get('length')
    length = int(length)
    inc_sym = request.json.get('includeSymbolsValue')
    inc_num = request.json.get('includeNumbersValue')
    inc_upp = request.json.get('includeUppercaseValue')


    print(length)
    print(inc_sym)
    print(inc_num)
    print(inc_upp)

    pw = ""
    n = 0

    while(n <= length):
        rand_num = random.randint(0, 3)

        if(rand_num == 0):
            random_letter = random.choice(string.ascii_letters)
            pw += random_letter.lower()
            n = n+1

        elif(inc_upp and rand_num == 1):
            random_letter = random.choice(string.ascii_letters)
            pw += random_letter.upper()
            n = n+1

        elif(inc_num and rand_num == 2):
            random_number = random.randint(0, 9)
            pw += str(random_number)
            n = n+1

        elif(inc_sym and rand_num == 3):
            symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
            random_symbol = random.choice(symbols)
            pw += random_symbol
            n = n+1
        
    return jsonify({'password': pw}), 200

if __name__ == '__main__':
    app.run(debug=True)