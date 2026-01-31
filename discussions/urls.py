from django.urls import path

from .views import (
    DiscussionCreateView,
    DiscussionDeleteView,
    DiscussionDetailView,
    DiscussionListView,
    DiscussionUpdateView,
)

app_name = 'discussions'

urlpatterns = [
    path('', DiscussionListView.as_view(), name='list'),
    path('new/', DiscussionCreateView.as_view(), name='create'),
    path('<int:pk>/', DiscussionDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', DiscussionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DiscussionDeleteView.as_view(), name='delete'),
]
