'''
include는 다른 urls.py 파일을 참조할 수 있도록 합니다.
만약 /polls/list/라는 주소로 접속하면 polls/까지는 잘라내고 list/부분만
polls/urls.py 에서 찾습니다.
'''


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),

]
