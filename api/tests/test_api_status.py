import unittest
import requests




class APITest(unittest.TestCase):

    API_URL = "http://127.0.0.1:5000"
    GET_TEST_RESULTS = "{}/testResults".format(API_URL)
    POST_TEST_RESULTS = "{}/addTestResult".format(API_URL)


    def test_get_all_test_reports(self):
        res = requests.get(APITest.GET_TEST_RESULTS)
        self.assertEqual(res.status_code, 200)


    def test_add_test_reports(self):
        params = {'squad': 'happy', 'status': 'passed', 'failedTests': 0}
        res = requests.post(APITest.POST_TEST_RESULTS, params=params)
        self.assertEqual(res.status_code, 200)


    def test_no_failedTests_success(self):
        params = {'squad': 'happy', 'status': 'passed'}
        res = requests.post(APITest.POST_TEST_RESULTS, params=params)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['noffailures'], 0)


    def test_no_squad_bad_request(self):
        params = {'status': 'passed', 'failedTests': 0}
        res = requests.post(APITest.POST_TEST_RESULTS, params=params)
        self.assertEqual(res.status_code, 400)


    def test_no_status_bad_request(self):
        params = {'squad': 'happy', 'failedTests': 0}
        res = requests.post(APITest.POST_TEST_RESULTS, params=params)
        self.assertEqual(res.status_code, 400)









