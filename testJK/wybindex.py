# -*- coding: UTF-8 -*-
import unittest
import requests
import json

class test_http(unittest.TestCase):
    def setUp(self):
        self.get_url = \
            "http://172.16.7.143:27010/hospital_test/hospital/webservice/insureService/querySendPolicyInfoCount.json"
    def test_get(self):
        session = requests.session()
        canshu = {'insType':'',
                  '_':''}
        rq = session.get("http://172.16.7.143:27010/hospital_test/hospital/webservice/insureService/querySendPolicyInfoCount.json",
                        params = canshu)
        code = rq.status_code
        self.assertTrue(code == 200,'code is error!')
        r_json = rq.json()
        self.assertEqual(r_json.get('insType'),'A')
        print r_json
    def tearDown(self):
        pass
if  __name__ == "__main__":
    unittest.main

