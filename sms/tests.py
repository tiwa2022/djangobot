from django.test import TestCase
import sqlite3

# Create your tests here.

from sms.models import Order


class SMSTests(TestCase):
    def test_for_json_support(self):
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT JSON(\'{"a": "b"}\')')
            self.assertIs(False, False)
        except:
            self.assertIs(True, False, "no support for json in sqlite3")
    def test_welcome(self):
        oOrder = Order(phone = '123-456-7890', data={"state":"WELCOMING"})
        aReturn = oOrder.handleInput("hello")
        self.assertEqual(aReturn[0], "Welcome to Rich's pizza", "welcome message line 1")
        self.assertEqual(aReturn[1], "Would you like a SMALL, MEDIUM, or LARGE?", "welcome message line 2")
        self.assertEqual(oOrder.getState(), "SIZE", "order state should be SIZE")
