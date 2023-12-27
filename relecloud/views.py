import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.messages.views import SuccessMessageMixin
from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import OpinionForm
from .models import Cruise, Destination, Opinion
from relecloud import models


# Vista para mostrar la página principal
def index(request):
    return render(request, "index.html")


# Vista para mostrar la página "about"
def about(request):
    return render(request, "about.html")


# Vista para mostrar los destinos
def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, "destinations.html", {"destinations": all_destinations})


# Vista para servir imágenes
def serve_image(request, destination_id):
    destination = get_object_or_404(Destination, pk=destination_id)
    image_path = os.path.join(
        settings.BASE_DIR,
        "relecloud",
        "static",
        "res",
        "img",
        "cruceros",
        f"{destination.name}.jpg",
    )
    return FileResponse(open(image_path, "rb"), content_type="image/jpg")


# Vista para mostrar las opiniones de un crucero
@csrf_exempt
def opinions(request, cruise_id):
    cruise = get_object_or_404(Cruise, pk=cruise_id)
    opinions = Opinion.objects.filter(cruise=cruise)

    if request.method == "POST":
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.cruise = cruise

            if request.user.is_authenticated:
                opinion.user = request.user
            else:
                # Si el usuario no está autenticado, asigna un usuario "Anónimo"
                opinion.user_id = 3

            opinion.save()

    else:
        form = OpinionForm()

    return render(
        request, "opinions.html", {"cruise": cruise, "opinions": opinions, "form": form}
    )  # Renderiza la plantilla


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
