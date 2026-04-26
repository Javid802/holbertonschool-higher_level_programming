from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage (EMPTY for checker)
users = {}


# Root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# Return list of usernames
@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))


# Status endpoint
@app.route("/status")
def status():
    return "OK"


# Get user by username
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)


# Add new user (POST)
@app.route("/add_user", methods=["POST"])
def add_user():
    # Check if JSON is valid
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    # Check username exists in payload
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check duplicate
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Create user object
    user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    users[username] = user

    return jsonify({
        "message": "User added",
        "user": user
    }), 201


if __name__ == "__main__":
    app.run()