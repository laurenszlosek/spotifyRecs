# https://www.youtube.com/watch?v=7LNl2JlZKHA
# // to start: 
# // npm start
from flask import Flask, request, render_template

app = Flask(__name__)

# Member
@app.route("/songs")
# def members() can fetch artist name and return for 
def songs():
    return {"songs": ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5"]}

if __name__ == "__main__":
    app.run(debug=True)