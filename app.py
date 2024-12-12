from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

todo_list = []

@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    todo_list.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['GET'])
def delete_task(task_id):
    if 0 < task_id <= len(todo_list):
        todo_list.pop(task_id - 1)
    return redirect(url_for('index'))

if __name__ == '_main_':
    app.run(debug=True)