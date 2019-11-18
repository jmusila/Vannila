import os
import unittest


from app.app import create_app


class TestQuestions(unittest.TestCase):
    def Setup(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

        self.question = {

        }

    def test_get_welcome_message(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_get_all_question(self):
        pass

    def test_post_question(self):
        pass

    def test_get_single_question(self):
        pass

    def tearDown(self):
        return super().tearDown()
