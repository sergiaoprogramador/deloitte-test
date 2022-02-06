import uuid
from django.db import models


class File(models.Model):
    path = models.FileField(upload_to="uploads/")
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, max_length=100)

    def __str__(self):
        return f"{self.path}"