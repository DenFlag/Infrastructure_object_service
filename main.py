from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///infrastructure_facilities_6.db'

db = SQLAlchemy(app)

class Infrastructure_facility(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_object = db.Column(db.String(50))
    address = db.Column(db.String(50))

    def __init__(self, name_of_object, address):
        self.name_of_object = name_of_object
        self.address = address

with app.app_context():
    db.create_all()

@app.route('/add_Infrastructure_facility', methods=['POST'])
def add_Infrastructure_facility():
    name_of_object = request.form['name_of_object']
    address = request.form['address']
    infrastructure_facility = Infrastructure_facility(name_of_object, address)
    db.session.add(infrastructure_facility)
    db.session.commit()
    return{"session": "Infrastructure_facility added successfully"}

@app.route('/get_Infrastructure_facility/<int:id>')
def get_Infrastructure_facility(id):
    infrastructure_facility = Infrastructure_facility.query.get(id)
    if infrastructure_facility:
        return jsonify({
            'id': infrastructure_facility.id,
            'name_of_object': infrastructure_facility.name_of_object,
            'address': infrastructure_facility.address
        })
    else:
        return {'error': 'Employee not found pososi'}

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)
