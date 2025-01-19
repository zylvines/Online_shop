from django.db import models

# Create your models here.

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Kategoriya nomi")
    slug = models.SlugField(unique=True, verbose_name="Kategoriya slug")

    def str(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Mahsulot nomi")
    description = models.TextField(blank=True, null=True, verbose_name="Mahsulot tavsifi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Kategoriya")
    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Asl narx")
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Chegirma narxi")
    is_on_sale = models.BooleanField(default=False, verbose_name="Chegirmada")
    image = models.ImageField(upload_to="product_images/", blank=True, null=True, verbose_name="Rasm")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")
    rating = models.FloatField(default=0.0, verbose_name="Reyting")
    likes = models.PositiveIntegerField(default=0, verbose_name="Yoqtirishlar soni")

    def final_price(self):
        return self.discount_price if self.is_on_sale and self.discount_price else self.original_price

    def str(self):
        return self.name
class PriceDiscount(models.Model):
    product_name = models.CharField(max_length=255, verbose_name="Mahsulot nomi")
    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Asl narx")
    discount_percentage = models.FloatField(verbose_name="Chegirma foizi", help_text="0 dan 100 gacha foiz qiymat")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")

    @property
    def discounted_price(self):
        discount = (self.original_price * self.discount_percentage) / 100
        return self.original_price - discount

    def str(self):
        return self.product_name