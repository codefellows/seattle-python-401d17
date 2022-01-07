from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy
from .models import Thing


class ThingListView(ListView):
    template_name = "thing_list.html"
    model = Thing


class ThingDetailView(DetailView):
    template_name = "thing_detail.html"
    model = Thing


class ThingCreateView(CreateView):
    template_name = "thing_create.html"
    model = Thing
    fields = ["name", "rating", "reviewer", "category"]


class ThingDeleteView(DeleteView):
    template_name = "thing_delete.html"
    model = Thing
    success_url = reverse_lazy("thing_list")


class ThingUpdateView(UpdateView):
    template_name = "thing_update.html"
    model = Thing
    fields = ["name", "rating"]


class AboutPageView(TemplateView):
    template_name = "about.html"
