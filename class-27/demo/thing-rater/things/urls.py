from django.urls import path
from .views import (
    ThingListView,
    ThingDetailView,
    AboutPageView,
)  # or * (use judiciously)

urlpatterns = [
    path("", ThingListView.as_view(), name="thing_list"),
    path("<int:pk>/", ThingDetailView.as_view(), name="thing_detail"),
    path("about/", AboutPageView.as_view(), name="about"),
]
