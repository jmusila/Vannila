from flask import Flask, request, jsonify
from config import app_config


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    Questions = []

    @app.route("/")
    def welcome():
        return "Welcome to StackOverflow-Lite API!"

    @app.route("/questions", methods=['GET'])
    def get_all_questions():
        return jsonify({"Status":"Ok", "Questions" : Questions}), 200

    @app.route("/questions", methods=['POST'])
    def post_question():
        data =request.get_json()
        id = len(Questions) + 1
        title = data['title']
        description = data['description']
        body = data['body']
        Question = {
            "id": id,
            "title": title,
            "description": description,
            "body": body
        }

        Questions.append(Question)
        return jsonify({"Status": "Ok", 'Message': "The Question was added successfully"}), 201


    def get_one(id):
        for i in Questions:
            if i['id'] == id:
                return i

    @app.route("/questions/<int:id>", methods=['GET'])
    def get_question_by_id(id):
        x = get_one(id)
        if x:
            return jsonify({"Status": "Ok", "Question": x}), 200
        return jsonify({"Message" : "Question with that id not found", "Status" : "Error"}), 404 

    @app.route("/questions/<int:id>", methods=['PUT'])
    def edit_question(id):
        x = get_one(id)
        if x:
            x.update(l)
            return jsonify({"Message": "Question updated successfully", "Status": "ok"}), 201
        return jsonify({"Message" : "Question with that id not found", "Status" : "Error"}), 404

    @app.route("/questions/<int:id>", methods=['DELETE'])
    def delete_question(id):
        x = get_one(id)
        if x:
            Questions.remove(x)
            return jsonify({"Status": "Ok", "Message": "Question Deleted Successfully"}), 204
        return jsonify({"Message" : "Question with that id not found", "Status" : "Error"}), 404

    return app