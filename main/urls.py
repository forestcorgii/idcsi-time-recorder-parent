from django.urls import path

from . import views

urlpatterns = [
    path('user/',views.createOrUpdate),
    path('user/<int:pk>/',views.SnippetDetail.as_view()),
    path('sync/',views.sync),

]
