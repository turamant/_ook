from django.conf import settings
from django.db import models
from django.urls import reverse



class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=120, default="N/A")
    slug = models.SlugField(max_length=120)
    nickname = models.CharField(max_length=120, default="N/A")
    email = models.CharField(max_length=120, default="N/A")
    phone = models.CharField(max_length=20, default="N/A")
    address = models.TextField(default="N/A")
    image = models.ImageField(
        upload_to='note/',
        null=True,
        blank=True)

    def __unicode__(self):
        return self.fullname

    def __str__(self):
        return self.fullname

    def __get_absolute_url(self):
        return reverse('detail', kwargs={"slug":self.slug})

    class Meta:
        ordering = ["fullname"]