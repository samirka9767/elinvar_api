import unittest
import requests
import json



class APITest(unittest.TestCase):

    API_URL = "http://127.0.0.1:5000/"
    GET_TEST_RESULTS = "{}/testResults".format(API_URL)
    POST_TEST_RESULTS = "{}/addTestResult".format(API_URL)
    MOCKED_TEST_REPORT = {
        "id": 1861,
        "squad_id": 1,
        "status": 1,
        "date": "06/11/2019",
        "failed_tests": 3
    }

    def test_get_all_test_reports(self):
        res = requests.get(APITest.GET_TEST_RESULTS)
        print(res.json())
        self.assertEqual(res.status_code, 200)

    def test_add_test_reports(self):
        print(APITest.POST_TEST_RESULTS)
        print(json.dumps(APITest.MOCKED_TEST_REPORT))
        res = requests.post(APITest.POST_TEST_RESULTS, json=json.dumps(APITest.MOCKED_TEST_REPORT))
        print(response.status_code)
        self.assertEqual(res.status_code, 200)



