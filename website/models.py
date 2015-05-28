from django.db import models
import uuid


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Room Name", max_length=100)
    image = models.ImageField("Picture", upload_to="img")
    price = models.IntegerField("Cost per night")
    description = models.TextField("Description", max_length=1000)

    def __str__(self):
        return self.name

    def cost(self):
        return "$%i/night" % self.price
