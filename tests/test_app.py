import os
import unittest
import json

from app.app import create_app


class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

        self.question = {
            "id": 1,
            "title": "This is the test question title",
            "description": "This is the description",
            "body": "The question body then"
        }

    def test_get_welcome_message(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_get_all_question(self):
        res = self.client.get("/questions")
        self.assertEqual(res.status_code, 200)

    def test_post_question(self):
        res = self.client.post("/questions", content_type='application/json', data=json.dumps(self.question))
        self.assertEqual(res.status_code, 201)
        self.assertIn('The Question was added successfully', str(res.data))

    def test_get_single_question(self):
        self.client.post("/questions", content_type='application/json', data=json.dumps(self.question))
        response = self.client.get("/questions/1")
        self.assertEqual(response.status_code, 200)

    def test_get_non_existence_question(self):
        res = self.client.get("questions/2")
        self.assertEqual(res.status_code, 404)
        self.assertIn('Question with that id not found', str(res.data))

    def test_update_question(self):
        self.client.post("/questions", content_type='application/json', data=json.dumps(self.question))
        response = self.client.put("questions/1")
        self.assertEqual(response.status_code, 201)
        self.assertIn('Question updated successfully', str(response.data))


    def test_delete_question(self):
        self.client.post("/questions", content_type='application/json', data=json.dumps(self.question))
        response = self.client.delete("questions/1")
        self.assertEqual(response.status_code, 204)
    
    def test_put_no_question(self):
        response = self.client.put("questions/1")
        self.assertEqual(response.status_code, 404)

    def test_delete_no_question(self):
        response = self.client.delete("questions/1")
        self.assertEqual(response.status_code, 404)


    def tearDown(self):
        return super().tearDown()
