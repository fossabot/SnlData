import unittest
import pytest
import requests
from module import snldata

class TestSnlData(unittest.TestCase):

    def setUp(self):
        self.service = snldata.SnlSession()
        super().setUp()

    def tearDown(self):
        self.service.close()

    def test_SimpleReq(self):
        self.G = requests.Session()
        self.test = self.G.get("https://snl.no/api/v1/search?query=")
        self.assertEqual(self.test.status_code,200)

    def test_Query(self):
        self.service.search(query="aa-", best=True)
        self.assertEqual( self.service.title, "aa-")

    def test_Query2(self):
        self.service.searchV2({"encyclopedia": "snl", "query": "aa-", "limit": 3, "offset": 0 }, zone="prototyping", best=True)
        self.assertEqual( self.service.title, "aa-")

    def test_search(self):
        self.service.search(query="NTNU")
        self.service._get(1)
        self.assertEqual( self.service.title, "NTNU Universitetsbiblioteket")

    def test_search2(self):
        self.service.searchV2({"encyclopedia": "snl", "query": "NTNU", "limit": 3, "offset": 0 }, zone="prototyping")
        self.service._get(1)
        self.assertEqual( self.service.title, "NTNU Universitetsbiblioteket")

if __name__ == '__main__':
    unittest.main()
