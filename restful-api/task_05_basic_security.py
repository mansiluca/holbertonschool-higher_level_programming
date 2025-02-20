#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'your-strong-secret-key'
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Basic protected route"""
    return "Basic Auth: Access Granted"

@jwt.unauthorized_loader
def handle_unauthorized_error(_):
    """Unauthorized loader"""
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(_):
    """Invalid token loader"""
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(_):
    """Expired token loader"""
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(_):
    """Revoked token loader"""
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(_):
    """Needs fresh token loader"""
    return jsonify({"error": "Fresh token required"}), 401

@auth.verify_password
def verify_password(username, password):
    """Verify password"""
    if username in users:
        if check_password_hash(users[username]['password'], password):
            return users[username]
    return None


@app.route("/login", methods=["POST"])
def login():
    """Login route"""
    if not request.is_json:
        return jsonify(), 400

    data = request.get_json()
    username = data.get("username", None)
    password = data.get("password", None)

    if not username or not password:
        return jsonify(), 400

    user = users.get(username, None)
    if not user or not check_password_hash(user["password"], password):
        return jsonify(), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """JWT protected route"""
    return "JWT Auth: Access Granted"

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Admin only route"""
    current_user = get_jwt_identity()
    if users[current_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted", 200

if __name__ == '__main__':
    app.run()
