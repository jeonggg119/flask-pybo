from flask import Blueprint, render_template, url_for, current_app
from werkzeug.utils import redirect
from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
@bp.route('/')
def index():
    #3/0
    #current_app.logger.info("INFO 레벨로 출력")
    return redirect(url_for('question._list'))


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)