from django.urls import path
from .views import *

urlpatterns = [
    path("", BookmarkListView.as_view(), name='list'),
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),
]

# 클래스형 뷰일 경우 as_view() 써야함
# <int:pk> 사이트뒤에 숫자는 migrations 테이블의 primary_key 의미 (id)