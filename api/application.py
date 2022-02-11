from flask import request
from datetime import date
from utilities.helper_functions import subtract_dates, set_verdict_status
from db_functions import Squad, Test_Reports, db, app, get_test_reports



# GET /testResults?squad=happy&daysToFollow=7
@app.route('/testResults', methods=['GET'])
def get_test_results_with_parameters():
    arr = {}
    totalFailedDays = 0
    daysToFollow = int(request.args.get("daysToFollow")) if request.args.get("daysToFollow") else 1000
    records = get_test_reports(request.args.get("squad"), request.args.get("daysToFollow"))
    print(records)
    for record in records:
        totalFailedDays += record.status
        arr.update({record.date: {"status": record.status, "noffailrues": record.failed_tests}})

    lastFailureUnfixedDays = subtract_dates(records[len(records) - 1].date) if len(records) !=0 else 0
    verdict = set_verdict_status(totalFailedDays, daysToFollow)
    arr.update({"totalDaysfailed": totalFailedDays})
    arr.update({"verdict": verdict})
    arr.update({"lastFailureUnfixedDays": lastFailureUnfixedDays})
    return {"details": arr}



# POST /addTestResult
@app.route('/addTestResult', methods=['POST'])
def add_test_results():
    args = request.args
    noffailures = int(args.get("failedTests"))
    status = ["passed", "failed"]
    today = date.today()
    squad = Squad.query.filter_by(name=args.get("squad")).first()
    if squad == None or (args.get("status") not in status):
        return {"400": "Bad request"}
    record = Test_Reports(squad_id=squad.id, date=str(today.strftime("%m/%d/%Y")), status=status.index(args.get("status")), failed_tests=noffailures)
    # record = Test_Reports(squad_id=squad.id, date="01/05/2020", status=status.index(args.get("status")), failed_tests=noffailures)
    db.session.add(record)
    db.session.commit()
    return {"id": record.id, "squad_id": record.squad_id, "date": record.date, "status": record.status,
            "noffailures": record.failed_tests}
