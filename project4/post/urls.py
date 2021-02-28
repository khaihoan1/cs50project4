from django.urls import path, reverse
from .views import PostCreateView, detail, PostDetailView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('create/', login_required(PostCreateView.as_view()), name="post_create"),
    path("<str:pk>/", PostDetailView.as_view(), name="post_detail"),
    # path('edit/<str:pk>', PostEditView.as_view(), name="post_edit")
]