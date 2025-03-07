#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "Jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"uzername": "john", "name": "John", "age": 30, "city": "New York"},
    }

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    return jsonify(list(users.keys))

@app.route("/status")
def get_status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "user not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_data()
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 404
    
    users[data["username"]] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
