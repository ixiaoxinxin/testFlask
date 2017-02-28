# -*- coding: UTF-8 -*-
import unittest
import requests

class test_http(unittest.TestCase):
    def setUp(self):
        self.get_url = "http://apitest.huaxiafinance.com/newPage/coupon/transferIndexPage.spring"
    def test_get(self):
        session = requests.session()
        canshu = {'channelId':'C01020015','shareId':'60',''
                  'recommenderId':'NjJRNmt2MTNyNkZTUSt3TjhnYlNrVDlNNm1iUDd0aU5RRTdDSUtlNDdzOD0',
                  'couponIds':'NjJRNmt2MTNyNkVsU1RjVGMyWWNYRmpjL2VTOUVGanJGT2oxcWxxZVNHVT0',
                  'couponNum':'1','oid':'oaZWXuArg__JpEMngInBk1-tP8sw ' }
        r = session.get("http://apitest.huaxiafinance.com/newPage/coupon/transferIndexPage.spring",
                        params = canshu)
        code = r.status_code
        self.assertTrue(code == 200,'code is error!')
        print code
        r_json = r.json()
        self.assertEqual(r_json.get('couponNum'), 1)
        print r_json
    def tearDown(self):
        pass
if  __name__ == "__main__":
    unittest.main

