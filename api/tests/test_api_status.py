import unittest
import requests
import configparser

config = configparser.ConfigParser()
config.read('../config/api_uri.ini')
config = config['api_uri']
get_uri = "{}{}".format(config["API_URL"], config["GET_TEST_RESULTS"])
post_uri = "{}{}".format(config["API_URL"], config["POST_TEST_RESULTS"])


class APITest(unittest.TestCase):
    print(config)
    def test_get_all_test_reports(self):
        res = requests.get(get_uri)
        self.assertEqual(res.status_code, 200)

    def test_add_tests_with_all_parameters(self):
        res = requests.post(get_uri, params={'squad': 'happy', 'status': 'failed', 'failedTests': 5})
        self.assertEqual(res.status_code, 200)

    def test_no_failedTests_success(self):
        res = requests.post(post_uri, params={'squad': 'happy', 'status': 'passed'})
        self.assertEqual(res.status_code, 200)

    def test_no_squad_bad_request(self):
        res = requests.post(post_uri, params={'status': 'passed', 'failedTests': 0})
        self.assertEqual(res.status_code, 400)

    def test_no_status_bad_request(self):
        res = requests.post(post_uri, params={'squad': 'happy', 'failedTests': 0})
        self.assertEqual(res.status_code, 400)
