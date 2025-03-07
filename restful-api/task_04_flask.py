#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"},
}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))  # ✅ FIXED (Added parentheses)

@app.route("/status")
def get_status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404  # ✅ FIXED (Capitalized "User")

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()  # ✅ FIXED (Use get_json() instead of get_data())
    
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400  # ✅ FIXED (400 for bad request)

    users[data["username"]] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
