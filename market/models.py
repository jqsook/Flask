

class Item(db.Model):
    # THis field is required with sqlalchemy
    id = db.Column(db.Integer(), primary_key=True)
    # This sets limits on the information stored in the db
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024),
                            nullable=False, unique=True)

    def __repr__(self):
        # This makes the name that shows up the database custom to the name in the
        return f'Item {self.name}'
