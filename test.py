import unittest
from app import fun
class TestFun(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("login process")
        cls.user = "user1"
    @classmethod
    def tearDownClass(cls):
        print("logout process")
        cls.user=None

    def setUp(self):
        print("resolurce creation")
    def tearDown(self):
        print("delete resource")

    def test_10_20(self):
        print(self.user)
        act=fun(10,20)
        exp=30
        self.assertEqual(act, exp, "test_10_20 failed")
    def test_str1_str2(self):
        print(self.user)
        act=fun("str1","str2")
        exp="str1str2"
        self.assertEqual(act, exp, "test_str1_str2 failed")
    def test_str1_10(self):
        print(self.user)
        act=fun("str1",10)
        exp=None
        self.assertEqual(act,exp,"test_str1_10 failed")
    def test_10_str2(self):
        print(self.user)
        act=fun(10,"str2")
        exp=None
        self.assertEqual(act,exp,"test_10_str2 failed")

unittest.main()