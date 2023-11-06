from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Rooms(models.Model):
#     # user=models.ForeignKey(User,related_name='my_rooms',on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True)
#     # capacity = models.PositiveIntegerField(max_length=20,default=0)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Room"


class MyRoom(models.Model):
    user = models.ForeignKey(User, related_name="my_profile", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Room"


class Messages(models.Model):
    room = models.ForeignKey(MyRoom, related_name="messages", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if (
            self.content.strip()
        ):  # Check if content is not empty or only contains whitespace
            super(Messages, self).save(*args, **kwargs)

    class Meta:
        ordering = ("date_added",)
