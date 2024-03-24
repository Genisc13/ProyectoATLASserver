from marshmallow import fields
from app.ext import ma


class DroneSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    span = fields.Integer()
    created = fields.Integer()
    responsible = fields.String()
    rotors = fields.Nested('RotorSchema', many=True)


class RotorSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
