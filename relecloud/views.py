import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import OpinionForm
from .models import Destination, Opinion
from relecloud import models
from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from . import models
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from .forms import OpinionForm


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
def opinions(request):
    if request.method == "POST":
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)

            if 1 <= opinion.rating <= 5:
                if request.user.is_authenticated:
                    opinion.user = request.user
                else:
                    # Si el usuario no está autenticado, asigna un usuario "Anónimo"
                    opinion.user_id = 3

                opinion.save()
                return redirect("opinions")  # Redirige a la página de opiniones
            else:
                form.add_error("rating", "El rating debe estar entre 1 y 5.")
        else:
            # El formulario no es válido, puedes mostrarlo nuevamente con los errores
            pass
    else:
        form = OpinionForm()

    opinions = Opinion.objects.all()
    return render(request, "opinions.html", {"opinions": opinions, "form": form})


class DestinationDetailView(DetailView):
    template_name = "destination_detail.html"
    model = models.Destination
    context_object_name = "destination"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_destination"] = True
        context["destination_photo"] = self.get_object().photo.url
        return context


class CruiseDetailView(generic.DetailView):
    template_name = "cruise_detail.html"
    model = models.Cruise
    context_object_name = "cruise"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cruise"] = self.get_object()
        return context


class InfoRequestCreate(SuccessMessageMixin, generic.CreateView):
    template_name = "info_request_create.html"
    model = models.InfoRequest
    fields = ["name", "email", "cruise", "notes"]
    success_url = reverse_lazy("index")
    success_message = (
        "Gracias, %(name)s! Te enviaremos más información sobre %(cruise)s!"
    )

    def form_valid(self, form):
        response = super().form_valid(form)

        # Envía un correo electrónico usando send_mail de Django
        subject = "Solicitud de Información"
        message = f'Hola {form.cleaned_data["name"]}, gracias por tu solicitud. Te enviaremos más información sobre {form.cleaned_data["cruise"]}.'
        from_email = (
            "relecloudd@gmail.com"  # Reemplaza con tu dirección de correo electrónico
        )
        recipient_list = [form.cleaned_data["email"]]

        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
        )

        return response
