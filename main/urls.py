from django.urls import path

from . import views

urlpatterns = [
    path('user/', views.user),
    # path('user/<int:pk>/', views.SnippetDetail.as_view()),
    path('sync/', views.sync),
]
