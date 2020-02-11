from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetView.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('user/', views.UserView.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

