from django.views.generic import TemplateView, ListView, DetailView
from .models import Thing


class ThingListView(ListView):
    template_name = "thing_list.html"
    model = Thing


class ThingDetailView(DetailView):
    template_name = "thing_detail.html"
    model = Thing


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
