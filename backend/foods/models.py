from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Food(Base):
    name = models.CharField(max_length=255, unique=True)
    quantity = models.PositiveIntegerField(null=False, blank=False, default=0)
    proteins = models.PositiveIntegerField(null=False, blank=False, default=0)
    carbohydrates = models.PositiveIntegerField(
        null=False, blank=False, default=0)
    fats = models.PositiveIntegerField(null=False, blank=False, default=0)

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'

    def __str__(self):
        return f"{self.name}"
