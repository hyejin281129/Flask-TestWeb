# blueprints : 라우트 함수 관리
# render_template : 템플릿 파일을 화면으로 렌더링
from flask import Blueprint, blueprints, render_template

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
  return 'Hello, Pybo!'

@bp.route('/')
def index():
  question_list = Question.query.order_by(Question.create_date.desc())
  return render_template('question/question_list.html', question_list=question_list)

