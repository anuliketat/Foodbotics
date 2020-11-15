from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

class ItemProfile(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    veg = models.BooleanField()
    ingredients = models.TextField(blank=True)
    recipe = models.TextField(blank=True)
    #price = models.DecimalField(decimal_places=2, max_digits=1000, blank=True, null=True)
    num_tasks = models.PositiveIntegerField(blank=True, null=True)
    stations = models.TextField(default='List of stations in order.', max_length=100)
    tasks = models.TextField(default='List of tasks in stations in order.', max_length=100)
    def __str__(self):
        return str(self.item)

class Prep_methods(models.Model):
    method = models.CharField(max_length=30)
    types = models.TextField(blank=True)
    about = models.URLField(default='https://en.wikipedia.org/wiki/Outline_of_food_preparation#Food_preparation_techniques')

    def __str__(self):
        return self.method



