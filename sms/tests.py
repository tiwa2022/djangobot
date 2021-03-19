from django.test import TestCase
import sqlite3

# Create your tests here.


class SMSTests(TestCase):
    def test_for_json_support(self):
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT JSON(\'{"a": "b"}\')')
            self.assertIs(False, False)
        except:
            self.assertIs(True, False)
