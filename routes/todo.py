from flask import render_template, redirect, Blueprint
from flask import request
from classes.todo_item import todo_manager
import re

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/todo', methods=['GET', 'POST'])
def todo(task=None):
    if request.method == 'GET':
        tasks = todo_manager().get_all()
        if len(tasks) == 0:
            todo_manager.truncate()
        return render_template('index.html', tasks=tasks)
    if request.method == 'POST':
        if (item := request.form.get('task')):
            todo_manager.create(item)

        if (item := request.form.get('task_complete')):
            index = re.findall(r'\d+', item)
            todo_manager.complete(int(index[0]))
            print(request.form.get('task_item'))

        if (item := request.form.get('task_delete')):
            index = re.findall(r'\d+', item)
            todo_manager.delete(int(index[0]))
            print(request.form.get('task_item'))
        return redirect("/todo")
   

