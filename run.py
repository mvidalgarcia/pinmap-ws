from flask import Flask
app = Flask(__name__)

@app.route('/pins/<user_google_id>', methods=['GET'])
def get_all_pins(user_google_id):
    return 'GET: All pins from ' + user_google_id

@app.route('/pin/<pin_id>', methods=['GET'])
def get_pin(pin_id):
    return 'GET: One pin id ' + pin_id

@app.route('/pin/<pin_id>', methods=['POST'])
def create_pin(pin_id):
    return 'POST: Create pin ' + pin_id

@app.route('/pin/<pin_id>', methods=['DELETE'])
def delete_pin(pin_id):
    return 'DELETE: Delete pin id ' + pin_id

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)