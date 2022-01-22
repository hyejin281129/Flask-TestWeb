from pybo import db

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

# Answer 클래스
class Answer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
  question = db.relationship('Question', backref=db.backref('answer_set'))
  content = db.Column(db.Text(), nullable=False)
  create_date = db.Column(db.DateTime(), nullable=False)

# User 클래스
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)