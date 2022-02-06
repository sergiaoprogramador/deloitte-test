from django.db import models
from cronos.support.base_model import BaseModel


class Post(BaseModel):
    content = models.TextField(null=True)
    cover_image = models.ForeignKey("cronos.File", db_index=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"{self.uuid} - {self.title}"

