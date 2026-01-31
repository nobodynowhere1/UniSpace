from django.urls import path

from .views import (
    LostFoundCreateView,
    LostFoundDeleteView,
    LostFoundDetailView,
    LostFoundListView,
    LostFoundUpdateView,
)

app_name = 'lostfound'

urlpatterns = [
    path('', LostFoundListView.as_view(), name='list'),
    path('new/', LostFoundCreateView.as_view(), name='create'),
    path('<int:pk>/', LostFoundDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', LostFoundUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', LostFoundDeleteView.as_view(), name='delete'),
]
