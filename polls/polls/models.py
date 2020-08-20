'''
쉽게 테이블과 컬럼을 만든다고 생각한다.
질문 모델 -> 질문 텍스트와, 날짜
선택 모델 -> 질문(Question에 소속되는 외래키) , 선택 텍스트, 투표

모델을 완성한 후
config/setting.py 에서 INSTALLED_APPS 윗줄에 추가한 후
python manage.py makemigrations polls 로 데이터 베이스에 적용시켜 준다.
'''

import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):  # 객체를 출력 할 때 나타날 내용.
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
