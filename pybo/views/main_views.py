# blueprints : 라우트 함수 관리
# render_template : 템플릿 파일을 화면으로 렌더링
from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

# @bp.route('/hello')
# def hello():
#   # return 'Hello, Pybo!'
#   return render_template('hello.html')



@bp.route('/')
def index():
  return render_template('hello.html')
  # return redirect(url_for('question._list'))

@bp.route('/main')
def main():
  return render_template('main/main.html')

@bp.route('/introduce')
def introduce():
  return render_template('main/introduce.html')