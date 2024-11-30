from flask import Blueprint, render_template, request, redirect, url_for, session
import random

math_problem_bp = Blueprint('math_problem', __name__)
math_problem_bp.secret_key = 'your_secret_key111'

@math_problem_bp.route('/', methods=['GET', 'POST'])
def math_problem():
    if 'score' not in session:
        session['score'] = 0

    if request.method == 'POST':
        first_num = int(request.form.get('first_num'))
        second_num = int(request.form.get('second_num'))
        user_answer = int(request.form.get('user_answer'))
        correct_answer = first_num + second_num

        if user_answer == correct_answer:
            session['score'] += 1
            if session['score'] >= 20:
                winning_score = True
                session.pop('score', None)  # Reset score
                return render_template('math_problem.html', winning_score=winning_score)
            return redirect(url_for('math_problem.math_problem'))
        else:
            return render_template('math_problem.html', first_num=first_num, second_num=second_num, correct_answer=correct_answer, score=session['score'])

    first_num = random.randint(1, 20)
    second_num = random.randint(1, 20)
    return render_template('math_problem.html', first_num=first_num, second_num=second_num, score=session['score'])
