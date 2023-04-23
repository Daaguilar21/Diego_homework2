from app import db
class Details(db.Model):
    code = db.Column(db.String(64), primary_key=True, unique=True, nullable=False)
    capital = db.Column(db.String(64), nullable=False)
    calling_code = db.Column(db.String(64), nullable=False)
    countryName = db.Column(db.String(64), nullable=False)
    
class Country(db.Model):
    code = db.Column(db.String(64), primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(64), unique=False, nullable=False)
    currency_code = db.Column(db.String(64), unique=False, nullable=False)

    def __repr__(self):
        return f"{self.name} ({self.code}): {self.currency_code}"

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    country_code = db.Column(db.String(64), nullable=False)
    country = db.Column(db.String(64), nullable=False)
    region = db.Column(db.String(64), nullable=False)

