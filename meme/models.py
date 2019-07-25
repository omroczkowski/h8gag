from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Meme(models.Model):
    CATEGORY_CHOICES = (
        ('LOL', 'LOL'),
        ('TFT', 'TFT'),
        ('SEX', 'SEX'),
    )
    description = models.CharField(max_length=100)
    rank = models.IntegerField(default = 0)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    meme_img = models.ImageField(upload_to='images/')

    upvoters = models.ManyToManyField(User, related_name="upvoters",)
    downvoters = models.ManyToManyField(User, related_name="downvoters",)

    def __unicode__(self):
        return self.description
    class Meta:
        ordering = ['date_added']






