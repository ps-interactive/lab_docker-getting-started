from flask import Flask, request, render_template, redirect
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        item = request.form.get('item')
        action = request.form.get('action')

        if action == 'Add':
            redis.rpush('todos', item)
        elif action == 'Remove':
            redis.lrem('todos', 1, item)

    items = redis.lrange('todos', 0, -1)
    return render_template('index.html', items=items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
