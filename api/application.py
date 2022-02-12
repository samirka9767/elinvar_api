from flask import request, abort 
from datetime import date
from utilities.helper_functions import subtract_dates, set_verdict_status
from db_functions import Squad, Test_Reports, db, app, get_test_reports, find_squad



@app.route('/testResults', methods=['GET'])
def get_test_results_with_parameters():
    (arr, totalFailedDays, daysToFollow, squad) = ({}, 0, request.args.get("daysToFollow"), request.args.get("squad"))
    daysToFollow = int(daysToFollow) if daysToFollow else 1000
    records = get_test_reports(squad, daysToFollow)
    for record in records:
        totalFailedDays += record.status
        arr.update({record.date: {"status": record.status, "noffailrues": record.failed_tests}})
    arr.update({"totalDaysfailed": totalFailedDays})
    arr.update({"verdict": set_verdict_status(totalFailedDays, daysToFollow)})
    arr.update({"lastFailureUnfixedDays": subtract_dates(records[len(records) - 1].date) if len(records) !=0 else 0})
    return {"details": arr}



@app.route('/addTestResult', methods=['POST'])
def add_test_results():
    #remove later
    args = request.args
    (squad, status, failedTests) = (request.args.get("squad"), request.args.get("status"), request.args.get("failedTests"))
    status_ls = ["passed", "failed"]
    if squad is None or status is None: 
        abort(400, 'squad and status not found')
    squad_query = find_squad(squad)
    if squad_query == None:
        abort(400, 'no such squad exists')
    if status not in status_ls:
        abort(400, 'incorect status value entered')
    #will remove later    
    date__ = args.get("addDummyDates")
    print(type(failedTests))
    try:
        noffailures = int(failedTests) if failedTests is not None  else 0 
    except ValueError:
        abort(400, "failedTests must be decimal")
    today = date.today()
    # record = Test_Reports(squad_id=squad_query.id, date=str(today.strftime("%m/%d/%Y")), status=status_ls.index(status), failed_tests=noffailures)
    record = Test_Reports(squad_id=squad_query.id, date=date__, status=status_ls.index(status), failed_tests=noffailures)
    db.session.add(record)
    db.session.commit()
    return {"id": record.id, "squad_id": record.squad_id, "date": record.date, "status": record.status,
            "noffailures": record.failed_tests}
