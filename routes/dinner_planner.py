from flask import render_template, redirect, Blueprint
from flask import request

dinner_planner_bp = Blueprint('dinnerplanner', __name__)

@dinner_planner_bp.route('/dinnerplanner', methods=['GET', 'POST'])
def dinnerplanner():
    if request.method == 'GET':
        return render_template('dinnerplanner.html')