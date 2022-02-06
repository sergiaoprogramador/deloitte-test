import uuid
from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, max_length=100)

    class Meta:
        abstract = True
        indexes = [models.Index(fields=["id"])]
