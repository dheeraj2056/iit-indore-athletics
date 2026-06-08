from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Athlete(db.Model):
    __tablename__ = "athletes"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    role = db.Column(db.String(50))

    dob = db.Column(db.String(20))
    blood = db.Column(db.String(10))

    height = db.Column(db.String(20))
    weight = db.Column(db.Float)

    program = db.Column(db.String(100))
    department = db.Column(db.String(100))

    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    pemail = db.Column(db.String(100))

    jersey = db.Column(db.String(100))
    events = db.Column(db.Text)

    comps = db.Column(db.Text)
    achieve = db.Column(db.Text)

    join = db.Column(db.String(20))
    shoe = db.Column(db.String(20))

    notes = db.Column(db.Text)


class Assessment(db.Model):
    __tablename__ = "assessments"

    id = db.Column(db.Integer, primary_key=True)

    athlete_id = db.Column(db.Integer)

    date = db.Column(db.String(20))

    acc = db.Column(db.Float)
    spd = db.Column(db.Float)
    agi = db.Column(db.Float)

    vj = db.Column(db.Float)
    bj = db.Column(db.Float)

    coop = db.Column(db.Float)
    fkm = db.Column(db.Float)

    thr = db.Column(db.Float)

    wt = db.Column(db.Float)
    lift = db.Column(db.Float)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))

    role = db.Column(db.String(20))
