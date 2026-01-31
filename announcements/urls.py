from django.urls import path

from .views import (
    AnnouncementCreateView,
    AnnouncementDeleteView,
    AnnouncementDetailView,
    AnnouncementListView,
    AnnouncementUpdateView,
)

app_name = 'announcements'

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='list'),
    path('new/', AnnouncementCreateView.as_view(), name='create'),
    path('<int:pk>/', AnnouncementDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', AnnouncementUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='delete'),
]
