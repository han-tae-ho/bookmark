from django.shortcuts import render

# Create your views here.
# CRUD : Create, Read, Update, Delete
# List

# 클래스형 뷰(제네릭 뷰), 함수형 뷰
# 웹페이지를 접속한다. -> 페이지를 본다
# url을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다. -> 응답

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from .models import Bookmark


class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkListView(ListView):
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_create'
    #방법1 : success_url 을 이용하는 방법
    success_url = reverse_lazy('list')


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'
    #방법 2: get_absolute url 을 이용하는 방법(모델에 설정)


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

