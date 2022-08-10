# line 3 to 4 - importing required libraries

from app import db
import uuid

# line 8 to 16 - making class 'Products'

class Products(db.Model):
    __tablename__ = "products" 
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String(64))
    image = db.Column(db.String(128))
    rating = db.Column(db.Integer)
    marked_price = db.Column(db.Float)
    selling_price = db.Column(db.Float)

    @staticmethod

    # line 22 to 33 - creating a function called 'create'

    def create(name, image, rating, marked_price, selling_price):
        product_dict = dict(
            guid = str(uuid.uuid4()),
            name = name,
            image = image,
            rating = rating,
            marked_price = marked_price,
            selling_price = selling_price
        )
        product_obj = Products(**product_dict)
        db.session.add(product_obj)
        db.session.commit()

    # line 37 to 40 - creating a function called 'update'

    def update(self, **details_dict):
        for k,v in details_dict.items():
            setattr(self, k, v)
        db.session.commit()