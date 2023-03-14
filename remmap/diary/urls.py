from django.urls import path
from . import views

urlpatterns = [
    path("", views.Diaries.as_view()),
    path("<int:pk>", views.DiaryDetail.as_view()),
]