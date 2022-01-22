from pybo import db


# 질문 추천 기능
question_voter = db.Table(
  'question_voter',
  db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
  db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
)

# 답변 추천 기능
answer_voter = db.Table(
  'answer_voter',
  db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
  db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)

# Question 클래스
class Question(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  subject = db.Column(db.String(200), nullable=False)
  content = db.Column(db.Text(), nullable=False)
  create_date = db.Column(db.DateTime(), nullable=False)
  # User 모델 데이터의 id 값을 Question 모델에 포함시킴
  user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
  # Question 모델에서 User모델을 참조함
  user = db.relationship('User', backref=db.backref('question_set'))
  # 수정 확인
  modify_date = db.Column(db.DateTime(), nullable=True)
  # 추천
  voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))

# Answer 클래스
class Answer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
  question = db.relationship('Question', backref=db.backref('answer_set'))
  content = db.Column(db.Text(), nullable=False)
  create_date = db.Column(db.DateTime(), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
  user = db.relationship('User', backref=db.backref('answer_set'))
  modify_date = db.Column(db.DateTime(), nullable=True)
  voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))

# User 클래스
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(150), unique=True, nullable=False)
  password = db.Column(db.String(200), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)

# Comment(댓글) 클래스
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('comment_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime())
    # 데이터베이스에서 질문 삭제 시 연관된 데이터도 삭제되게 하였음
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), nullable=True)
    question = db.relationship('Question', backref=db.backref('comment_set'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), nullable=True)
    answer = db.relationship('Answer', backref=db.backref('comment_set'))