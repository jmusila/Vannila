import os
import unittest
import json


from app import create_app

class TestQuestions(unittest.TestCase):
    def Setup(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

        self.question = {

        }

    def test_get_welcome_message(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()
