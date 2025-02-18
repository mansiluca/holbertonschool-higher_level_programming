#!/usr/bin/python3
"""
This module fetches posts from a RESTful
API and prints them to the console
"""


from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """
    This function returns a welcome message
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def route_data():
    """
    This function returns a JSON response
    """
    return jsonify(list(users.keys()))


@app.route('/info')
def route_info():
    """
    This function returns a JSON response
    """
    info = {"version": "1.0", "description": "A simple API built with Flask"}
    return jsonify(info)


@app.route('/status')
def route_status():
    """
    This function returns a JSON response
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    This function returns a JSON response
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    This function adds a user
    """
    if request.is_json:
        data = request.get_json()
        username = data.get('username')
        name = data.get('name')
        age = data.get('age')
        city = data.get('city')

        if not username:
            return jsonify({"error": "Username is required"}), 400

        users[username] = {
            "username": username,
            "name": name,
            "age": age,
            "city": city
        }
        return jsonify({
            "message": "User added",
            "user": users[username]
        }), 201
    else:
        return jsonify({"error": "Request must be JSON"}), 400


if __name__ == "__main__":
    app.run()
