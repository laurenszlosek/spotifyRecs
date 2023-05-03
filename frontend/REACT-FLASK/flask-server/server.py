# https://www.youtube.com/watch?v=7LNl2JlZKHA
# // to start: 
# make sure to be in client
# // npm start

# then:
# in flask-server
# source venv/bin/activate
# pip3 install flask
from flask import Flask, request, render_template

app = Flask(__name__)

# Member
@app.route("/songs")
# def songs() can fetch artist name and return for 
def songs():
    return {"songs": ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5"]}

# def userInputSong():
#     return {"singleSong": "songFromUser"}

if __name__ == "__main__":
    app.run(debug=True)