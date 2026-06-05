from django.urls import path
from .views import postlist, postdetail
app_name = "api-v1"

urlpatterns = [
    path("posts/",postlist,name="post-list"),
    path("posts/<int:id>/",postdetail,name="post-detail"),
]