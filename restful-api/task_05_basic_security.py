#!/usr/bin/env python3
"""
Flask API with Basic Authentication and JWT authentication.

Provides:
- Basic Authentication using HTTPBasicAuth
- JWT Authentication for token-based security
- Role-based access control for admin-only routes
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Initialize Flask app
app = Flask(__name__)

# Initialize Basic Authentication
auth = HTTPBasicAuth()

# Configure JWT authentication
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# User database (in-memory)
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    """
    Verify username and password for Basic Authentication.

    Args:
        username (str): The username provided by the user.
        password (str): The password provided by the user.

    Returns:
        str: The username if authentication is successful, False otherwise.
    """
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return False

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Protected route using Basic Authentication.

    Returns:
        JSON: A success message if authentication is successful.
    """
    return jsonify({"message": "Basic Auth: Access Granted"})

@app.route("/login", methods=["POST"])
def login():
    """
    Login route for JWT authentication.

    Expects:
        JSON body with "username" and "password".

    Returns:
        JSON: A JWT access token if login is successful, or an error message otherwise.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(users[username]["password"], password):
        # Generate JWT token with user identity (including role)
        token = create_access_token(identity={"username": username, "role": users[username]["role"]})
        return jsonify({"access_token": token})
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Protected route using JWT authentication.

    Returns:
        JSON: A success message if the JWT token is valid.
    """
    return jsonify({"message": "JWT Auth: Access Granted"})

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Admin-only protected route.

    Requires:
        - A valid JWT token
        - User must have "admin" role

    Returns:
        JSON: A success message if the user is an admin, or an error message otherwise.
    """
    user = get_jwt_identity()

    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return jsonify({"message": "Admin Access: Granted"}), 200

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle unauthorized access errors.

    Returns:
        JSON: A 401 error message if a JWT token is missing or invalid.
    """
    return jsonify({"error": "Missing or invalid token"}), 401

if __name__ == "__main__":
    app.run(debug=True)
