
# main.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tasks = request.form.getlist('task')
        time_slots = request.form.getlist('time_slot')
        return redirect(url_for('planner', tasks=tasks, time_slots=time_slots))
    return render_template('index.html')

@app.route('/planner', methods=['GET'])
def planner():
    tasks = request.args.getlist('tasks')
    time_slots = request.args.getlist('time_slots')
    return render_template('planner.html', tasks=tasks, time_slots=time_slots)

if __name__ == '__main__':
    app.run(debug=True)
