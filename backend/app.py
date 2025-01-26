from flask import Flask, render_template, request, jsonify
from scripts import *  # Assuming the necessary functions are in this module

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
global VARIABLES
VARIABLES = None

# Route to serve the HTML file
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the 'Solve' button functionality
@app.route('/solve', methods=['POST'])
def solve_route():
    # Get the problem data from the frontend
    data = request.get_json()
    problem = data.get('problem', '')
    print('solve button clicked')

    # Solve the problem and get the solution and steps
    solution, steps, variables = solve(problem)
    print(solution)
    global VARIABLES
    VARIABLES = variables

    # Return the solution and steps as JSON
    return jsonify({
        'solution': solution,
        'steps': steps,
        'message': 'Solution calculated!'
    })

# Route to handle the 'Show Steps' button functionality
@app.route('/show-steps', methods=['POST'])
def show_steps_route():
    return show_steps()  # Call the show_steps function from scripts.py


if __name__ == '__main__':
    app.run(debug=True)
