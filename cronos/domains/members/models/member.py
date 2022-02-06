from django.db import models
from cronos.support.base_model import BaseModel


class Member(BaseModel):
    about = models.TextField(null=True)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    profile_picture = models.ForeignKey(
        "cronos.File", db_index=True, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"{self.uuid} - {self.first_name} {self.last_name}"
