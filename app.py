# to run- in terminal:
# cd frontend
# python3 -m venv venv
# source venv/bin/activate
# (only once) pip3 install flask
# flask run or python3 -m flask run
from flask import Flask, render_template, request
# from main import Backend

app = Flask(__name__)
# FC = Backend()

@app.route('/', methods=['GET', 'POST'])
def index():
    output_lines = []
    if request.method == 'POST':
        user_input = request.form['user_input']
        with open('user_input.txt', 'w') as f:
            f.write(user_input)
            # FC.main()
        output_lines = get_output_lines()
    return render_template('index.html', output_lines=output_lines)

def get_output_lines():
    with open('output.txt', 'r') as f:
        output_lines = f.readlines()
    return output_lines

if __name__ == '__main__':
    app.run(debug=True)