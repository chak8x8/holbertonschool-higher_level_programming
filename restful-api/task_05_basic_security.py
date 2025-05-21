#!/usr/bin/env python3
"""
Flask API with Basic Authentication and JWT authentication.
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
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # Use a strong key in production
jwt = JWTManager(app)

# User database (in-memory)
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Authentication."""
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return False

@auth.error_handler
def auth_error(status):
    """Handle Basic Authentication errors."""
    return jsonify({"error": "Unauthorized"}), 401

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Protected route using Basic Authentication."""
    return jsonify({"message": "Basic Auth: Access Granted"}), 200

@app.route("/login", methods=["POST"])
def login():
    """Login route for JWT authentication."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 401

    if username in users and check_password_hash(users[username]["password"], password):
        token = create_access_token(identity={"username": username, "role": users[username]["role"]})
        return jsonify({"access_token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Protected route using JWT authentication."""
    return jsonify({"message": "JWT Auth: Access Granted"}), 200

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Admin-only protected route."""
    user = get_jwt_identity()
    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200

# Custom JWT error handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
