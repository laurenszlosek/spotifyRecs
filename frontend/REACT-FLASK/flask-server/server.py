# https://www.youtube.com/watch?v=7LNl2JlZKHA
from flask import Flask, request, render_template

app = Flask(__name__)

# Member
@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}
if __name__ == "__main__":
    app.run(debug=True)