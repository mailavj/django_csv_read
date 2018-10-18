
# Create your models here.
from django.db import models
from django.utils import timezone


class Product(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    from_site = models.CharField(max_length=500)
    price = models.FloatField()
    text = models.TextField()

    added_date = models.DateTimeField(
            default=timezone.now)

    def added(self):
        self.added_date = timezone.now()
        self.save()

    def __str__(self):
        return self.type


class Csv_items(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=100)
    item_link = models.TextField()
    item_price = models.FloatField()


    def add_item(self):
        self.added_date = timezone.now()
        self.save()

    def __str__(self):
        return self.type
