# -*- coding: UTF-8 -*-
import unittest
import requests


class test_http(unittest.TestCase):
    def setUp(self):
        self.get_url = \
            "https://httpbin.org/get"
    def test_get(self):
        session = requests.session()
        canshu = {'key1':'value1',
                  'key2':'value2'}
        rq = session.get("https://httpbin.org/get",
                        params = canshu)
        code = rq.status_code
        self.assertTrue(code == 200,'code is error!')
        r_json = rq.json()
        self.assertEqual(r_json.get('success'),True)
        #self.assertEqual(r_json.get('key1'),'value1')
        print r_json
    def tearDown(self):
        pass
if  __name__ == "__main__":
    unittest.main

