from django.db import models
from django.conf import settings

class Provider(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    provider_name = models.CharField(max_length=50)
    def __str__(self):
        return self.provider_name

class Offer(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    coffee_name = models.CharField(max_length=20, default='')
    publication_date = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    def __str__(self):
        return '%s %s' % (self.provider, self.coffee_name)

