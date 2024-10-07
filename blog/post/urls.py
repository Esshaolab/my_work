# coding=utf-8
from django.urls import path, re_path
from .views import queryAll, detail, queryPostByCid, queryPostByCreated

urlpatterns=[
    re_path(r'^$',queryAll),
    re_path(r'^page/(\d+)$',queryAll),
    re_path(r'^post/(\d+)$',detail),
    re_path(r'^category/(\d+)$',queryPostByCid),
    re_path(r'^archive/(\d+)/(\d+)$',queryPostByCreated),
]