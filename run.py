from flask import Flask, request, jsonify

app = Flask(__name__)

Questions = []

@app.route("/")
def welcome():
    return "Welcome to StackOverflow-Lite!"

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


@app.route("/questions/<int:id>", methods=['GET'])
def get_question_by_id(id):
    for question in Questions:
        if question['id'] == id:
            return jsonify({"Status": "Ok", "Question": question}), 200
        else:
            return jsonify({"Message" : "Question with that id not found", "Status" : "Error"}), 404
    

if __name__ == "__main__":
    app.run(debug = True)