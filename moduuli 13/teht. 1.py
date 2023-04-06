from flask import Flask, jsonify
from prime_checker import is_prime

app = Flask(__name__)

@app.route('/alkuluku/<int:number>')
def check_prime(number):
    if is_prime(number):
        return jsonify({'Number': number, 'isPrime': True})
    else:
        return jsonify({'Number': number, 'isPrime': False})

if __name__ == '__main__':
    app.run(debug=True, port=3000)

