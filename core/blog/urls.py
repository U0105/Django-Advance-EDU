from django.urls import path
from blog.views import IndexView, RDview, CBListview


urlpatterns = [
    path("cbv-index",IndexView.as_view(),name="index"),
    path("rdv-index/<int:pk>",RDview.as_view(),name="rdv"),
    path("posts/",CBListview.as_view(),name="list_view"),
]