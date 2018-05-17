from mongoengine import *

#design database
#create collection
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    # weight = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
