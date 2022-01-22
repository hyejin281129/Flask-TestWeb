from datetime import datetime
from flask import Blueprint, url_for, request, render_template, g
from werkzeug.utils import redirect

from .. import db
from ..forms import AnswerForm 
from ..models import Question, Answer

# 데코레이션 함수 적용
from pybo.views.auth_views import login_required

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=('POST',))
@login_required
def create(question_id):
    # 답병 등록 폼
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        content = request.form['content']
        # 로그인 사용자 정보 추가
        answer = Answer(content=content, create_date=datetime.now(), user=g.user)
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    return render_template('question/question_detail.html', question=question, form=form)

