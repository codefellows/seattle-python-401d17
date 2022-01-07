from django.urls import path
from .views import (
    ThingListView,
    ThingDetailView,
    ThingCreateView,
    ThingDeleteView,
    ThingUpdateView,
    AboutPageView,
)  # or * (use judiciously)

urlpatterns = [
    path("", ThingListView.as_view(), name="thing_list"),
    path("create/", ThingCreateView.as_view(), name="thing_create"),
    path("<int:pk>/", ThingDetailView.as_view(), name="thing_detail"),
    path("<int:pk>/delete/", ThingDeleteView.as_view(), name="thing_delete"),
    path("<int:pk>/update/", ThingUpdateView.as_view(), name="thing_update"),
    path("about/", AboutPageView.as_view(), name="about"),
]
