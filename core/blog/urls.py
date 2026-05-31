from django.urls import path
from blog.views import IndexView, RDview, CBListview, CBDetailview, CBFormview, Cpostcreate

app_name = 'blog'

urlpatterns = [
    path("cbv-index",IndexView.as_view(),name="index"),
    path("rdv-index/<int:pk>",RDview.as_view(),name="rdv"),
    path("posts/",CBListview.as_view(),name="list_view"),
    path("posts/<int:pk>/",CBDetailview.as_view(),name="detail_view"),
    path("posts/newcat",CBFormview.as_view(),name="form_view"),
    path("posts/newpost",Cpostcreate.as_view(),name="create_view"),
]