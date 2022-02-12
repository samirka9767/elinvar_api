from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trt.db'
db = SQLAlchemy(app)


class Squad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f"new squad was added: {self.id} - name: {self.name}"


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    squad_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(15), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    failed_tests = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Record was added {self.id} - squad_id : {self.squad_id}; date - {self.date} -status: {self.status} -failed_tests: {self.failed_tests}"


class Test_Reports(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    squad_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(15), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    failed_tests = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Record was added {self.id} - squad_id : {self.squad_id}; date - {self.date} -status: {self.status} -failed_tests: {self.failed_tests}"


def get_test_reports(squad, daysToFollow):
    query = Test_Reports.query
    print("\n")
    print("\n")
    print("\n")
    print("1st one: ",query.all())
    if not squad and not daysToFollow:
        return query.order_by(Test_Reports.id.desc()).all()

    if squad:
        squad_query = find_squad(squad)
        if squad_query:
            query = query.filter_by(squad_id=squad_query.id)
        else: 
            return []

    query = query.order_by(Test_Reports.id.desc())

    if daysToFollow:
        print("daysToFollow",daysToFollow)
        query = query.limit(daysToFollow)
        print("after days limit ",query.all())
    
    return query.all()


def find_squad(squad):
    return Squad.query.filter_by(name=squad).first()
