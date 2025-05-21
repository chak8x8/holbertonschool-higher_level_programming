#!/usr/bin/env python3
"""
Flask API with Basic Authentication and JWT authentication.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt

# Initialize Flask app
app = Flask(__name__)

# Initialize Basic Authentication
auth = HTTPBasicAuth()

# Configure JWT authentication
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # Change this in your application!
jwt = JWTManager(app)

# User database (in-memory)
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Authentication."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None # Return None instead of False as per Flask-HTTPAuth docs for clarity

@auth.error_handler
def auth_error(status):
    """Handle Basic Authentication errors."""
    # The status argument is provided by Flask-HTTPAuth, usually 401 or 403
    return jsonify({"error": "Missing or invalid credentials"}), 401 # Ensure it's always 401 for auth failure

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Protected route using Basic Authentication."""
    return jsonify({"message": "Basic Auth: Access Granted"})

@app.route("/login", methods=["POST"])
def login():
    """Login route for JWT authentication."""
    data = request.get_json()

    # Add check for non-JSON or empty request body
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Request must be a JSON object"}), 400 # Or 401 if strictly auth error

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 401

    user_data = users.get(username)
    if user_data and check_password_hash(user_data["password"], password):
        # Embed username and role in the token's identity
        # Or more detailed claims in additional_claims
        access_token = create_access_token(identity=username, additional_claims={"role": user_data["role"]})
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Protected route using JWT authentication."""
    return jsonify({"message": "JWT Auth: Access Granted"})

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Admin-only protected route."""
    # current_user_identity = get_jwt_identity() # This gets what was passed to `identity` in create_access_token
    jwt_claims = get_jwt() # This gets the full JWT payload, including additional_claims
    
    user_role = jwt_claims.get("role")

    if user_role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})

# Custom JWT error handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err_description): # Argument is an error description string
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err_description): # Argument is an error description string
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload): # Corrected signature
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload): # Corrected signature
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload): # Corrected signature
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
