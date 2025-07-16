from django.db import models
from django.contrib.auth.models import User

class Calculation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expression = models.CharField(max_length=255)
    result = models.CharField(max_length=100)
    not_deleted = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.expression} = {self.result}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        calculations = Calculation.objects.filter(not_deleted=True).order_by('-created')
        if calculations.count() > 10:
            for calc in calculations[10:]:
                calc.not_deleted = False
                calc.save()
