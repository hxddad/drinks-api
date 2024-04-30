from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return "Hello World"

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    res = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.descripton }
        res.append(drink_data)
    return {"drinks": res}

def create_db():
    with app.app_context():
        db.create_all()
        print("Database tables created successfully.")

@app.route('/drinks/<id>')

def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {'name': drink.name, 'description': drink.descripton}

@app.route('/drinks', methods=['POST'])

def add_drink(name, description):
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}

@app.route('/drinks', methods=['DELETE'])

def delete_drink(id):
    if drink is None:
        return {"error", "not found"}
    drink = Drink.query.get(id)
    db.session.delete(drink)
    db.session.commit()
    return {"message": "Deleted."}

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
