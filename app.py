from flask import Flask, render_template, request
from main import Backend
import subprocess
app = Flask(__name__)
backend = Backend()
@app.route('/', methods=['GET', 'POST'])
def index():
    output_lines = []
    if request.method == 'POST':
        user_input = request.form['user_input']
        with open('user_input.txt', 'w') as f:
            f.write(user_input)
        run_main()
        output_lines = get_output_lines()
    return render_template('index.html', output_lines=output_lines)

def get_output_lines():
    with open('output.txt', 'r') as f:
        output_lines = f.readlines()
    return output_lines

def run_main():
    subprocess.check_output(['python', '-c', 'from main import Backend; Backend().main()'])

if __name__ == '__main__':
    app.run(debug=True)
