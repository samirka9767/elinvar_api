import unittest
import requests



class APIData(unittest.TestCase):

    API_URL = "http://127.0.0.1:5000"
    GET_TEST_RESULTS = "{}/testResults".format(API_URL)
    POST_TEST_RESULTS = "{}/addTestResult".format(API_URL)


    def test_results_num_equal_daysToFollow(self):
        params = {'squad': 'happy', 'daysToFollow': 4}
        res = requests.get(APIData.GET_TEST_RESULTS, params=params)
        res_json = res.json()
        json_length = len(res_json['details'])
        if json_length > 3:
            self.assertGreater(params['daysToFollow'], json_length-3)


    def test_results_not_existing_squad(self):
        params = {'squad': 'incorrect_name'}
        res = requests.get(APIData.GET_TEST_RESULTS, params=params)
        self.assertEqual(len(res.json()['details']), 3)


    def test_add_test_reports(self):
        params = {'squad': 'happy', 'status': 'failed', 'failedTests': 3}
        res = requests.post(APIData.POST_TEST_RESULTS, params=params)
        self.assertEqual(res.status_code, 200)
