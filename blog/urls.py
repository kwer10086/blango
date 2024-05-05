from django.urls import path,include
from blog import views

urlpatterns= [
  path("",views.index,name="index"),
  path("ip/",views.get_id,name="get_id"),
  path("post_detail/<slug>/",views.post_detail,name="post_detail"),
]

