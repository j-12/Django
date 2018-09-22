from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=100)
    product_image = models.CharField(max_length=200)
    product_price = models.CharField(max_length=20)
    def __str__(self):
        return self.product_name


# Create your models here.
class user_info(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return 'Name:' + self.name + ' Password:' + self.password

class Cart(models.Model):
    cart_product_name = models.CharField(max_length=50)
    cart_product_price = models.CharField(max_length=20)

    def __str__(self):
        return self.cart_product_name

# python manage.py shell
# info.objects.filter(name__startswith='so')
# info.objects.all()
# info.objects.filter(id=1)
# class Album(models.Model):
# 	artist=models.Charfield(max_length=50)
# 	genre=models.Charfield(max_length=50)
# 	album_title=models.Charfield(max_length=50)

# class Song(models.Model):
# 	album=models.ForeignKey(Album,on_delete=models.CASCADE)
# 	file_type=models.Charfield(max_length=10)
# 	song_title=models.Charfield(max_length=50)
