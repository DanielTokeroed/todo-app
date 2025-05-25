from flask import Blueprint, render_template
from flask import request
from classes.todo_item import todo_manager

todo_bp = Blueprint('index',__name__)

@todo_bp.route('/', methods=['GET','POST'])
def todo(task=None):
    if request.method == 'GET':
        t = todo_manager()
        print(t.get_all())
        return render_template('index.html')
    # if request.method == 'POST':
    #     t.create
   