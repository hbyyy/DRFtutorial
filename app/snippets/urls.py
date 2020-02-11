from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.SnippetView.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('user/', views.UserViewSet.as_view(), name='user-list'),
    path('user/<int:pk>/', views.UserViewSet.as_view(), name='user-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
