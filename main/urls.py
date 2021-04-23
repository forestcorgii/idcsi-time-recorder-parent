from django.urls import path

from . import views

urlpatterns = [
    path('home/',views.home),
    path('sync/',views.sync),
    path('<int:pk>/',views.SnippetDetail.as_view()),

]
