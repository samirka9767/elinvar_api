import unittest
import requests
import json



class APITest(unittest.TestCase):

    API_URL = "http://127.0.0.1:5000/"
    GET_TEST_RESULTS = "{}/testResults".format(API_URL)
    POST_TEST_RESULTS = "{}/addTestResult".format(API_URL)


    def test_get_all_test_reports(self):
        res = requests.get(APITest.GET_TEST_RESULTS)
        self.assertEqual(res.status_code, 200)

    def test_add_test_reports(self):
        res = requests.post(APITest.POST_TEST_RESULTS, data=json.dumps({"squad_id": 1, "status": 1, "date": "06/11/2019", "failed_tests": 3}))
        response = requests.post('https://httpbin.org/post', data=json.dumps({'id': 1, 'name': 'ram sharma'}))
        self.assertEqual(res.status_code, 200)



