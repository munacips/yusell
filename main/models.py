from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    description = models.TextField(max_length=1000)
    item_pic = models.ImageField(upload_to="pics/items/")
    date_listed = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name


class ItemPic(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    item_pic = models.ImageField(upload_to="pics/items/")