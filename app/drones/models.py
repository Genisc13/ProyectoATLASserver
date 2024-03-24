from app.db import db, BaseModelMixin


class Drone(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    span = db.Column(db.Integer)
    created = db.Column(db.Integer)
    responsible = db.Column(db.String)
    rotors = db.relationship('Rotor', backref='drone', lazy=False, cascade='all, delete-orphan')

    def __init__(self, name, span, created, responsible, rotors=None):
        if rotors is None:
            rotors = []
        self.name = name
        self.span = span
        self.created = created
        self.responsible = responsible
        self.rotors = rotors

    def __repr__(self):
        return f'Drone({self.title})'

    def __str__(self):
        return f'{self.title}'


class Rotor(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    drone_id = db.Column(db.Integer, db.ForeignKey('drone.id'), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Rotor({self.name})'

    def __str__(self):
        return f'{self.name}'
