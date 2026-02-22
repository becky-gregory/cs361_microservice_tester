"""
Microservice tester – serves the single-page UI and proxies requests to avoid CORS.
Run: python app.py
Then open http://127.0.0.1:5000
"""

import requests
from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path

app = Flask(__name__, static_folder=".")
APP_ROOT = Path(__file__).parent


@app.route("/")
@app.route("/index.html")
def index():
    return send_from_directory(APP_ROOT, "index.html")


@app.route("/social_create_activity.html")
def social_create_activity():
    return send_from_directory(APP_ROOT, "social_create_activity.html")


@app.route("/social_list_activities.html")
def social_list_activities():
    return send_from_directory(APP_ROOT, "social_list_activities.html")


@app.route("/social_get_feed.html")
def social_get_feed():
    return send_from_directory(APP_ROOT, "social_get_feed.html")


@app.route("/social_create_follow.html")
def social_create_follow():
    return send_from_directory(APP_ROOT, "social_create_follow.html")


@app.route("/social_list_follows.html")
def social_list_follows():
    return send_from_directory(APP_ROOT, "social_list_follows.html")


@app.route("/social_delete_follow.html")
def social_delete_follow():
    return send_from_directory(APP_ROOT, "social_delete_follow.html")


@app.route("/social_list_following.html")
def social_list_following():
    return send_from_directory(APP_ROOT, "social_list_following.html")


@app.route("/social_list_followers.html")
def social_list_followers():
    return send_from_directory(APP_ROOT, "social_list_followers.html")


@app.route("/social_like_activity.html")
def social_like_activity():
    return send_from_directory(APP_ROOT, "social_like_activity.html")


@app.route("/social_list_activity_likes.html")
def social_list_activity_likes():
    return send_from_directory(APP_ROOT, "social_list_activity_likes.html")


@app.route("/social_unlike_activity.html")
def social_unlike_activity():
    return send_from_directory(APP_ROOT, "social_unlike_activity.html")


@app.route("/notification_create_notification.html")
def notification_create_notification():
    return send_from_directory(APP_ROOT, "notification_create_notification.html")


@app.route("/notification_list_notifications.html")
def notification_list_notifications():
    return send_from_directory(APP_ROOT, "notification_list_notifications.html")


@app.route("/notification_update_notification.html")
def notification_update_notification():
    return send_from_directory(APP_ROOT, "notification_update_notification.html")


@app.route("/notification_get_unread_count.html")
def notification_get_unread_count():
    return send_from_directory(APP_ROOT, "notification_get_unread_count.html")


@app.route("/user_list_users.html")
def user_list_users():
    return send_from_directory(APP_ROOT, "user_list_users.html")


@app.route("/user_get_user.html")
def user_get_user():
    return send_from_directory(APP_ROOT, "user_get_user.html")


@app.route("/user_create_user.html")
def user_create_user():
    return send_from_directory(APP_ROOT, "user_create_user.html")


@app.route("/user_update_user.html")
def user_update_user():
    return send_from_directory(APP_ROOT, "user_update_user.html")


@app.route("/api/call", methods=["POST"])
def proxy_call():
    """Forward request to the selected microservice and return the response."""
    data = request.get_json(force=True, silent=True) or {}
    base_url = (data.get("baseUrl") or "").rstrip("/")
    method = (data.get("method") or "GET").upper()
    path = data.get("path") or "/"
    query = data.get("query") or {}
    body = data.get("body")

    if not base_url:
        return jsonify({"error": "baseUrl is required"}), 400

    url = f"{base_url}{path}"
    headers = {"Content-Type": "application/json"} if body and method in ("POST", "PUT", "PATCH") else {}

    try:
        resp = requests.request(
            method,
            url,
            params=query,
            json=body if body else None,
            headers=headers,
            timeout=10,
        )
        return jsonify({
            "status": resp.status_code,
            "headers": dict(resp.headers),
            "body": resp.text,
        }), 200
    except requests.RequestException as e:
        return jsonify({
            "error": str(e),
            "status": None,
            "body": None,
        }), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
