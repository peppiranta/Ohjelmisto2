from flask import Flask, jsonify
from airport_database import airport_db

app = Flask(__name__)

@app.route('/kenttä/<string:icao>')
def get_airport_data(icao):
    airport = airport_db.get(icao.upper())
    if airport:
        return jsonify({
            'ICAO': airport['icao'],
            'Name': airport['name'],
            'Municipality': airport['municipality']
        })
    else:
        return jsonify({'error': f'ICAO code {icao} not found'})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
