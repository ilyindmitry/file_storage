from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import dummy
from django.core.signals import request_finished

class UserFile(models.Model):
    upload_datetime = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    file = models.FileField(null=True)


    FILE_STATUS = (
        ('r', 'ready'),
        ('p', 'pending'),
    )

    status = models.CharField(max_length=1, choices=FILE_STATUS)

    class Meta:
        ordering = ["upload_datetime"]

    def __str__(self):
        return '{0}'.format(self.file.name)


@receiver(post_save, sender=UserFile)
def update_userfile_state(sender, instance, created, **kwargs):
    if created:
        dummy(instance)
        instance.status = 'r'
        instance.save()
