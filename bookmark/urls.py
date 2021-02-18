from django.urls import path
from .views import BookmarkListView

urlpatterns = [
    path("", BookmarkListView.as_view(), name='list')
    # 클래스형 뷰일 경우 as_veiw() 써야함
]