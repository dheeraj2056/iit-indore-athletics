from flask import Flask, render_template, request, jsonify
from config import Config
from models import db, Athlete, Assessment, User

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
with app.app_context():

    db.create_all()

    default_users = [

    ("coach1", "samsir", "coach"),
    ("coach2", "baggasir", "coach"),

    ("ep230051005@iiti.ac.in", "temp123", "head"),
    ("me240003066@iiti.ac.in", "temp123", "cohead"),
    ("me240003057@iiti.ac.in", "temp123", "mentor"),

    ("ee220002023@iiti.ac.in", "temp123", "athlete"),
    ("me220003055@iiti.ac.in", "temp123", "athlete"),
    ("phd1901261005@iiti.ac.in", "temp123", "athlete"),

    ("ee240002068@iiti.ac.in", "temp123", "athlete"),
    ("phd2301121009@iiti.ac.in", "temp123", "athlete"),

    ("mems250005013@iiti.ac.in", "temp123", "athlete"),
    ("cse250001022@iiti.ac.in", "temp123", "athlete"),

    ("me250003064@iiti.ac.in", "temp123", "athlete"),
    ("me250003033@iiti.ac.in", "temp123", "athlete"),

    ("mc250041012@iiti.ac.in", "temp123", "athlete"),

    ("me250003018@iiti.ac.in", "temp123", "athlete"),
    ("me250003012@iiti.ac.in", "temp123", "athlete"),

    ("phd2501201005@iiti.ac.in", "temp123", "athlete"),
    ("mt2502171025@iiti.ac.in", "temp123", "athlete"),
    ("me250003079@iiti.ac.in", "temp123", "athlete"),
]

    for username, password, role in default_users:

        existing = User.query.filter_by(
            username=username
        ).first()

        if not existing:

            user = User(
                username=username,
                password=password,
                role=role
            )

            db.session.add(user)

    db.session.commit()

@app.route("/")
def home():
    return render_template("index.html")


# =====================================
# LOGIN
# =====================================

@app.route("/api/login", methods=["POST"])
def login():

    data = request.json

    user = User.query.filter_by(
        username=data.get("username"),
        password=data.get("password")
    ).first()

    if not user:

        return jsonify({
            "success": False
        })

    return jsonify({
        "success": True,
        "role": user.role
    })
@app.route("/api/change-password", methods=["POST"])
def change_password():

    data = request.json

    username = data.get("username")
    old_password = data.get("old_password")
    new_password = data.get("new_password")

    user = User.query.filter_by(
        username=username,
        password=old_password
    ).first()

    if not user:
        return jsonify({
            "success": False,
            "message": "Wrong password"
        })

    user.password = new_password

    db.session.commit()

    return jsonify({
        "success": True
    })


# =====================================
# ATHLETES
# =====================================

@app.route("/api/athletes", methods=["GET"])
def get_athletes():

    athletes = Athlete.query.all()

    return jsonify([
        {
            "id": a.id,

            "name": a.name,
            "role": a.role,

            "dob": a.dob,
            "blood": a.blood,

            "height": a.height,
            "weight": a.weight,

            "program": a.program,
            "dept": a.department,

            "phone": a.phone,
            "email": a.email,
            "pemail": a.pemail,

            "jersey": a.jersey,
            "events": a.events,

            "comps": a.comps,
            "achieve": a.achieve,

            "join": a.join,
            "shoe": a.shoe,

            "notes": a.notes
        }
        for a in athletes
    ])


@app.route("/api/athletes", methods=["POST"])
def add_athlete():

    data = request.json

    athlete = Athlete(
        name=data.get("name"),
        role=data.get("role"),

        dob=data.get("dob"),
        blood=data.get("blood"),

        height=data.get("height"),
        weight=data.get("weight"),

        program=data.get("program"),
        department=data.get("dept"),

        phone=data.get("phone"),
        email=data.get("email"),
        pemail=data.get("pemail"),

        jersey=data.get("jersey"),
        events=data.get("events"),

        comps=data.get("comps"),
        achieve=data.get("achieve"),

        join=data.get("join"),
        shoe=data.get("shoe"),

        notes=data.get("notes")
    )

    db.session.add(athlete)
    db.session.commit()

    return jsonify({
        "success": True,
        "id": athlete.id
    })


@app.route("/api/athletes/<int:id>", methods=["PUT"])
def update_athlete(id):

    athlete = Athlete.query.get_or_404(id)

    data = request.json

    athlete.name = data.get("name", athlete.name)
    athlete.role = data.get("role", athlete.role)

    athlete.dob = data.get("dob", athlete.dob)
    athlete.blood = data.get("blood", athlete.blood)

    athlete.height = data.get("height", athlete.height)
    athlete.weight = data.get("weight", athlete.weight)

    athlete.program = data.get("program", athlete.program)
    athlete.department = data.get("dept", athlete.department)

    athlete.phone = data.get("phone", athlete.phone)
    athlete.email = data.get("email", athlete.email)
    athlete.pemail = data.get("pemail", athlete.pemail)

    athlete.jersey = data.get("jersey", athlete.jersey)
    athlete.events = data.get("events", athlete.events)

    athlete.comps = data.get("comps", athlete.comps)
    athlete.achieve = data.get("achieve", athlete.achieve)

    athlete.join = data.get("join", athlete.join)
    athlete.shoe = data.get("shoe", athlete.shoe)

    athlete.notes = data.get("notes", athlete.notes)

    db.session.commit()

    return jsonify({
        "success": True
    })


@app.route("/api/athletes/<int:id>", methods=["DELETE"])
def delete_athlete(id):

    athlete = Athlete.query.get_or_404(id)

    db.session.delete(athlete)
    db.session.commit()

    return jsonify({
        "success": True
    })


# =====================================
# ASSESSMENTS
# =====================================

@app.route("/api/assessments", methods=["GET"])
def get_assessments():

    assessments = Assessment.query.all()

    return jsonify([
        {
            "id": a.id,

            "memberId": a.athlete_id,
            "date": a.date,

            "acc": a.acc,
            "spd": a.spd,
            "agi": a.agi,

            "vj": a.vj,
            "bj": a.bj,

            "coop": a.coop,
            "fkm": a.fkm,

            "thr": a.thr,

            "wt": a.wt,
            "lift": a.lift
        }
        for a in assessments
    ])


@app.route("/api/assessments", methods=["POST"])
def add_assessment():

    data = request.json

    assessment = Assessment(
        athlete_id=data.get("athlete_id"),
        date=data.get("date"),

        acc=data.get("acc"),
        spd=data.get("spd"),
        agi=data.get("agi"),

        vj=data.get("vj"),
        bj=data.get("bj"),

        coop=data.get("coop"),
        fkm=data.get("fkm"),

        thr=data.get("thr"),

        wt=data.get("wt"),
        lift=data.get("lift")
    )

    db.session.add(assessment)
    db.session.commit()

    return jsonify({
        "success": True
    })


@app.route("/api/assessments/<int:id>", methods=["DELETE"])
def delete_assessment(id):

    assessment = Assessment.query.get_or_404(id)

    db.session.delete(assessment)
    db.session.commit()

    return jsonify({
        "success": True
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
