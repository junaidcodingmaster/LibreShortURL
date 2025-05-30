from flask import Flask, request, jsonify, redirect, g, render_template , send_file
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import os
import requests
from dotenv import load_dotenv

from sql_db import SQL_DB
from WORDS_NOVA import generate_word

CONFIG_PATH = "./config.env"
load_dotenv(CONFIG_PATH)

DB_PATH = "./db/urls.db"
BLACKLIST_FILE = "./db/blacklist-urls.txt"

if os.path.exists("./config.env"):
    REQ_LIMIT_PER_DAY = os.getenv("REQ_LIMIT_PER_DAY")
    SERVER_DOMAIN = os.getenv("SERVER_DOMAIN")
    SERVER_HOST = os.getenv("SERVER_HOST")
    SERVER_PORT = os.getenv("SERVER_PORT")
else:
    REQ_LIMIT_PER_DAY = 50
    SELF_DOMAIN = "/"
    SERVER_HOST = "localhost"
    SERVER_PORT = 5000


db = SQL_DB()

# Load blacklist
BLACKLIST = []

if os.path.exists(BLACKLIST_FILE):
    with open(BLACKLIST_FILE, "r") as f:
        BLACKLIST = [line.strip() for line in f]
else:
    print(f"[ERROR] Blacklist file '{BLACKLIST_FILE}' not found.")
    # Handle the error as needed


# Helper function to get a database connection per request
def get_db():
    if "db_conn" not in g:
        g.db_conn = db.connect_db(DB_PATH)
    return g.db_conn


# Helper function to store data
def store_data(data=()):
    conn = get_db()
    db.insert_data(
        conn=conn,
        insert_sql="INSERT INTO LibreShortUrlsDB (url, name) VALUES (?, ?)",
        data_tuple=data,
    )


# Helper function to check if a URL is reachable
def check_rejected_url_available(url, data):
    try:
        res = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
            },
            verify=True,
        )
        status = res.status_code
    except Exception:
        status = 500

    if status == 404:
        return (
            f"<h1>REJECTION PAGE NOT FOUND</h1>\n"
            f"<b>Report :</b>\n"
            f"<code style='color:white;background-color:black;'>\n"
            f"Status Code : {status}\n"
            f"Rejection URL : {url}\n"
            f"</code>",
            404,
        )
    elif status == 200:
        return data
    else:
        return (
            f"<h1 style='color:red;'>DANGER : Rejection page is not secure!</h1>\n"
            f"<h2>Unable to connect/check/ping the rejection URL</h2>\n"
            f"<b>Report :</b>\n"
            f"<code style='color:white;background-color:black;'>\n"
            f"Status Code : {status}\n"
            f"Rejection URL : {url}\n"
            f"</code>\n"
            f"<p>Go Back the rejection URL {url} , can be Malware , trap , scam, Server down or etc</p>"
        )


# Initialize Flask app
app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app)


# Close the database connection after each request
@app.teardown_appcontext
def close_db(error):
    db_conn = g.pop("db_conn", None)
    if db_conn is not None:
        db_conn.close()


@app.route("/")
def index():
    return render_template("index.html")


# Route to generate a shortened URL
@app.route("/api/gen-url", methods=["POST"])
@limiter.limit(f"{REQ_LIMIT_PER_DAY} per day")
def output_gen_URL():
    data = request.json
    url = data.get("url", "").strip()
    name = data.get("name", "").strip()

    # Validation
    if len(url) == 0:
        return jsonify({"message": "URL is missing!"}), 400

    if len(name) == 0:
        name = generate_word()

    if len(name) >= 18:
        return jsonify({"message": "Too Long"}), 401

    # Blacklist check
    for blocked in BLACKLIST:
        if blocked in name:
            return jsonify({"message": "NOT ALLOWED"}), 401

    # Check if name already exists
    conn = get_db()
    names = db.query_data(conn=conn, query_sql="SELECT name FROM LibreShortUrlsDB")

    for (registered_name,) in names:
        if name == registered_name:
            return jsonify({"message": f"{name} - Already exists!"}), 500

    # Store the data
    store_data((url, name))
    return (
        jsonify(
            {
                "message": "URL successfully Created and hosted.",
                "url": f"{SERVER_DOMAIN}/{name}",
            }
        ),
        200,
    )


# Route to redirect to the original URL
@app.route("/<name>", methods=["GET"])
def rejection(name):
    conn = get_db()
    data = db.query_data(conn=conn, query_sql="SELECT * FROM LibreShortUrlsDB")

    if name == "index.js":
        return send_file("./templates/index.js")
    elif name == "styles.css":
        return send_file("./templates/styles.css")

    for _, url, registered_name in data:
        if name == registered_name:
            return check_rejected_url_available(url, redirect(url, code=308))

    return "404 Not Found", 404


# Route to check if a name is available
@app.route("/api/check-name-availability", methods=["POST"])
def check_url_availability():
    name = (request.json).get("name", "").strip()

    conn = get_db()
    names = db.query_data(conn=conn, query_sql="SELECT name FROM LibreShortUrlsDB")

    # Validation
    if len(name) == 0:
        name = generate_word()
        print("name :", name)

    if len(name) >= 18:
        return jsonify({"message": "Too Long"}), 401

    # Blacklist
    for blocked in BLACKLIST:
        if name in blocked:
            return jsonify({"message": "NOT ALLOWED"}), 200

    for (registered_name,) in names:
        if name == registered_name:
            return jsonify({"message": f"{name} - Already exists!"}), 200
        else:
            return jsonify({"message": f"{name} - Available!"}), 200


# Run the app
if __name__ == "__main__":
    app.run(host=SERVER_HOST, port=SERVER_PORT)
