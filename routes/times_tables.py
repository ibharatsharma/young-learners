from flask import Blueprint, render_template

times_tables_bp = Blueprint('times_tables', __name__)

@times_tables_bp.route('/')
def times_tables():
    times = {i: [i * j for j in range(1, 13)] for i in range(1, 21)}
    return render_template('times_tables.html', times=times)
