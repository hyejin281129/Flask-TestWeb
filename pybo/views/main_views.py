# blueprints : 라우트 함수 관리
# render_template : 템플릿 파일을 화면으로 렌더링
from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello():
  # return 'Hello, Pybo!'
  return render_template(url_for('hello.html'))

@bp.route('/')
def index():
  return redirect(url_for('question._list'))
