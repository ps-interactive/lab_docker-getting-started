from flask import Flask, request, redirect, url_for
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, db=0)


@app.route('/', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = request.form.get('task')
        r.rpush('tasks', task)
    tasks = [task.decode('utf-8') for task in r.lrange('tasks', 0, -1)]
    tasks_html = ''.join(
        f'<li>{task} <form method="post" action="{url_for("delete")}"><input type="hidden" name="task" value="{task}"><input type="submit" value="Delete"></form></li>' for task in tasks)
    return f'''
        <h1>Todo List</h1>
        <form method="post">
            <input type="text" name="task" required>
            <input type="submit" value="Add Task">
        </form>
        <ul>{tasks_html}</ul>
    '''


@app.route('/delete', methods=['POST'])
def delete():
    task = request.form.get('task')
    r.lrem('tasks', 1, task.encode('utf-8'))
    return redirect(url_for('todo'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
