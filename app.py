from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Sample task data (simulated database)
tasks = [
    {'id': 1, 'title': 'Buy groceries', 'description': 'Milk, Bread, Butter', 'done': False, 'time': ''},
    {'id': 2, 'title': 'Clean house', 'description': 'Living room, Kitchen', 'done': False, 'time': ''},
]

# Utility function to find a task by its ID
def get_task_by_id(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

# Route to render the homepage with all tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        # Get the data from the form
        title = request.form['title']
        description = request.form['description']
        time = request.form['time']

        # Create a new task and add it to the task list
        new_task = {
            'id': len(tasks) + 1,  # Simple auto-incrementing ID
            'title': title,
            'description': description,
            'done': False,
            'time': time
        }
        tasks.append(new_task)

        # Optionally, redirect back to add more tasks or to the homepage
        return redirect(url_for('add_task'))  # Stay on the Add Task page after adding

    return render_template('add_task.html')

# Route to edit a task (GET to display, POST to update)
@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = get_task_by_id(task_id)
    
    if request.method == 'POST':
        # Update the task's title, description, and time
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        task['time'] = request.form['time']
        return redirect(url_for('index'))  # Redirect back to the task list

    if task:
        return render_template('edit_task.html', task=task)
    return "Task not found", 404

# Route to delete a task
@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = get_task_by_id(task_id)
    if task:
        tasks.remove(task)  # Remove the task from the list
    return redirect(url_for('index'))  # Redirect to the homepage after deletion

if __name__ == '__main__':
    app.run(debug=True)
