#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Sample Users
users = {
    "user1": {"password": generate_password_hash("password"), "role": "user"},
    "admin1": {"password": generate_password_hash("adminpass"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return False

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(users[username]["password"], password):
        token = create_access_token(identity={"username": username, "role": users[username]["role"]})
        return jsonify({"access_token": token})

    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return jsonify({"message": "JWT Auth: Access Granted"})

@app.route("/admin-only")
@jwt_required()
def admin_only():
    user = get_jwt_identity()
    
    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return jsonify({"message": "Admin Access: Granted"})

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

if __name__ == "__main__":
    app.run(debug=True)
