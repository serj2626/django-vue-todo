from django.db import models
from django.conf import settings


class TODO(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(null=True)
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='todos',
                             null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} for {self.user.username}'
