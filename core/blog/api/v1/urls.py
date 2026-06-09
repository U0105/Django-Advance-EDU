from django.urls import path
from blog.api.v1 import views
app_name = "api-v1"

urlpatterns = [
    # path("posts/",postlist,name="post-list"),
    path("posts/",views.PostList.as_view(),name="post-list"),
    # path("posts/<int:id>/",views.postdetail,name="post-detail"),
    path("posts/<int:id>/",views.PostDetail.as_view(),name="post-detail"),
]