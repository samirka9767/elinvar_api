import unittest
import requests
import configparser
from datetime import date


config = configparser.ConfigParser()
config.read('config/api_uri.ini')
config = config['api_uri']
get_uri = "{}{}".format(config["API_URL"], config["GET_TEST_RESULTS"])
post_uri = "{}{}".format(config["API_URL"], config["POST_TEST_RESULTS"])




class APIData(unittest.TestCase):

    def test_results_num_equal_daysToFollow(self):
        params = {'squad': 'happy', 'daysToFollow': 4}
        res = requests.get(get_uri, params=params)
        res_json = res.json()
        json_length = len(res_json['details'])
        if json_length > 3:
            self.assertGreater(params['daysToFollow'], json_length - 3)

    def test_results_not_existing_squad(self):
        res = requests.get(get_uri, params={'squad': 'incorrect_name'})
        self.assertEqual(len(res.json()['details']), 3)

    def test_incorrect_status_bad_request(self):
        res = requests.post(post_uri, params={'squad': 'happy', 'status': 'wrongStatus', 'failedTests': 0})
        self.assertEqual(res.status_code, 400)

    def test_add_test_reports_all_params(self):
        res = requests.post(post_uri, params={'squad': 'luna_team', 'status': 'failed', 'failedTests': 93})
        self.assertEqual(str(date.today().strftime("%m/%d/%Y")), res.json()['date'])




