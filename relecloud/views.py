from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from . import models
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from .forms import OpinionForm


# Create your views here.
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, "destinations.html", {"destinations": all_destinations})


def opinions(request, cruise_id):
    cruise = get_object_or_404(models.Cruise, pk=cruise_id)
    opinions = models.Opinion.objects.filter(cruise=cruise)

    if request.method == "POST":
        form = OpinionForm(request.POST)
        if form.is_valid():
            form.instance.cruise = cruise
            form.save()
            return redirect("opinions", cruise_id=cruise_id)
    else:
        form = OpinionForm()

    return render(
        request,
        "opinions.html",
        {"cruise": cruise, "opinions": opinions, "form": form},
    )


class DestinationDetailView(generic.DetailView):
    template_name = "destination_detail.html"
    model = models.Destination
    context_object_name = "destination"


class CruiseDetailView(generic.DetailView):
    template_name = "cruise_detail.html"
    model = models.Cruise
    context_object_name = "cruise"


class InfoRequestCreate(SuccessMessageMixin, generic.CreateView):
    template_name = "info_request_create.html"
    model = models.InfoRequest
    fields = ["name", "email", "cruise", "notes"]
    success_url = reverse_lazy("index")
    success_message = "Thank you, %(name)s! We will email you when we have more information about %(cruise)s!"
