from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("destinations/", views.destinations, name="destinations"),
    path(
        "destination/<int:pk>",
        views.DestinationDetailView.as_view(),
        name="destination_detail",
    ),
    path("cruise/<int:pk>", views.CruiseDetailView.as_view(), name="cruise_detail"),
    path("info_request", views.InfoRequestCreate.as_view(), name="info_request"),
    path("cruise/<int:cruise_id>/opinions", views.opinions, name="opinions"),
    path("opinions/", views.opinions, name="opinions"),
    path(
        "destination/<int:destination_id>/photo/",
        views.serve_image,
        name="destination_photo",
    ),
    path(
        "destination/<int:destination_id>/photo/",
        views.serve_image,
        name="destination_photo",
    ),
]

# Agrega la siguiente línea para servir archivos estáticos durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
