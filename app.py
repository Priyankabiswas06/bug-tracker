from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

def get_db():
    return sqlite3.connect("bugs.db")

@app.route("/", methods=["GET", "POST"])
def index():
    db = get_db()
    cursor = db.cursor()

    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        status = "Open"

        cursor.execute(
            "INSERT INTO bugs (title, description, status) VALUES (?, ?, ?)",
            (title, description, status)
        )
        db.commit()
        return redirect("/")

    cursor.execute("SELECT * FROM bugs ORDER BY id DESC")
    bugs = cursor.fetchall()
    return render_template("index.html", bugs=bugs)

if __name__ == "__main__":
    # Cloud-friendly run
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
