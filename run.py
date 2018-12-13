from flask import Flask, request, jsonify

app = Flask(__name__)

Questions = []

@app.route("/")
def welcome():
    return "Welcome to StackOverflow-Lite!"

@app.route("/questions", methods=['GET'])
def get_all_questions():
    return jsonify({"Questions" : Questions}), 200

if __name__ == "__main__":
    app.run(debug = True)