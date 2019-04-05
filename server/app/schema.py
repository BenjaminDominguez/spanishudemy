from marshmallow import Schema, ValidationError, fields, pre_load
from app.models import User

#custom function for future use
def must_not_be_blank(data):
    if not data:
        raise ValidationError("Data not provided")

class UserSchema(Schema):
    #dump only because we do not want to PUT or POST a new ID, this is done oncce and auto-incrementally
    id = fields.Int(dump_only=True)
    username = fields.Str()
    password = fields.Str()

"""
Instantiating Schema, this is temporary, might move it over
to main __init__.py file or load into a function
"""

user_schema = UserSchema()

#get schema for multiple users
users_schema = UserSchema(many=True)
