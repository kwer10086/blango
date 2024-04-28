from django.urls import path
from blog import views
urlpatterns= [
  path("",views.index,name="index"),
  path("post_detail/<slug>/",views.post_detail,name="post_detail"),
]