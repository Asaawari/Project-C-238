# line 3 to 4 - importing required libraries

from app import db
import uuid

# line 8 to 15 - making class 'Tickets'

class Tickets(db.Model):
    __tablename__ = "tickets"
    id = db.Column(db.Integer, primary_key=True) 
    guid = db.Column(db.String, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(64))
    description = db.Column(db.String(1024))
    attachment = db.Column(db.String(64))

    @staticmethod

    # line 21 to 31 - creating a function called 'create'

    def create(user_id, title, description, attachment):
        ticket_dict = dict(
            guid = str(uuid.uuid4()),
            user_id = user_id,
            title = title,
            description = description,
            attachment = attachment
        )
        ticket_obj = Tickets(**ticket_dict)
        db.session.add(ticket_obj)
        db.session.commit()

    # line 35 to 38 - creating a function called 'update'

    def update(self, **details_dict):
        for k,v in details_dict.items():
            setattr(self, k, v)
        db.session.commit()