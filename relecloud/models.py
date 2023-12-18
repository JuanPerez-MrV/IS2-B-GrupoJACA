from django.db import models


class Destination(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,
    )
    description = models.TextField(max_length=2000, null=False, blank=False)
    image = models.ImageField(
        upload_to="destination_images/", null=True, blank=True
    )  # Campo de imagen

    def __str__(self):
        return self.name


class Cruise(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,
    )
    description = models.TextField(max_length=2000, null=False, blank=False)
    destinations = models.ManyToManyField(Destination, related_name="cruises")

    def __str__(self):
        return self.name


class InfoRequest(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    email = models.EmailField()
    notes = models.TextField(
        max_length=2000,
        null=False,
        blank=False,
        default="",  # default es optional
    )
    cruise = models.ForeignKey(Cruise, on_delete=models.PROTECT)


class Opinion(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    comment = models.TextField(
        max_length=2000,
        null=False,
        blank=False,
    )
    rating = models.IntegerField(
        null=False,
        blank=False,
        validators=[models.Min(1), models.Max(5)],  # Rango de valores para el rating
    )
    cruise = models.ForeignKey(Cruise, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} - {self.cruise.name}"
