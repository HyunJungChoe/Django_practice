'''
    path 함수는 path(route, view, kwargs, name)형태로 호출한다.
    주소 , 호출할 뷰, 뷰에 전달할 값, route의 이름 순서이다.
    name은 config/urls.py 파일에 연결해야 동작한다.
'''

from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.result, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # /polls/5/vote 식.  <>는 변수를 의미한다.

]