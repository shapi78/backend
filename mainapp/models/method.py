import uuid

from django.db import models
from mainapp.models import DataSourceMethod


class Method(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    dataset = models.ForeignKey(
        "Dataset",
        on_delete=models.CASCADE,
        related_name="methods",
        null=False,
        blank=False,
    )
    salt_key = models.UUIDField(
        unique=True, null=False, blank=False, default=uuid.uuid4
    )
    group_age_over = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "methods"
        unique_together = ("dataset", "name")

    @property
    def state(self):
        data_source_methods = DataSourceMethod.objects.filter(method_id=self.id)
        data_source_methods_states = {"error": 0, "pending": 0, "ready": 0}

        for dsrc_method in data_source_methods:
            data_source_methods_states[dsrc_method.state] += 1

        if data_source_methods_states["pending"]:
            return "pending"

        if not data_source_methods_states["ready"]:
            return "error"

        return "ready"
