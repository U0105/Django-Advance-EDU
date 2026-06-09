from django.urls import path
from blog.api.v1 import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register("posts",views.PostModelViewSet,basename="posts")
router.register("categorys",views.CategoryModelSet,basename="categorys")
urlpatterns = router.urls

"""
urlpatterns = [
    # path("posts/",postlist,name="post-list"),
    path("posts/",views.PostList.as_view(),name="post-list"),
    # path("posts/<int:id>/",views.postdetail,name="post-detail"),
    path("posts/<int:id>/",views.PostDetail.as_view(),name="post-detail"),
]
"""