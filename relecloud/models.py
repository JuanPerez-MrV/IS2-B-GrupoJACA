from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Destination(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,
    )
    description = models.TextField(max_length=2000, null=False, blank=False)
    photo = models.ImageField(upload_to="res/img/cruceros/", null=False, blank=False)

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
    destinations = models.ManyToManyField("Destination", related_name="cruises")

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(
        max_length=2000,
        null=False,
        blank=False,
    )
    rating = models.IntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    def __str__(self):
        return f"{self.user.username} - Rating: {self.rating}"
