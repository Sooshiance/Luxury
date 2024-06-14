from django.db import models
from django.core.validators import RegexValidator


######################################## Product section ########################################


class Category(models.Model):
    title       = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    thumbnail   = models.ImageField(upload_to='category/')
    active      = models.BooleanField(default=True)
    created_at  = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        managed = True
        ordering = ['-created_at']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    numbers         = RegexValidator(r'^[0-9a]*$', message='تنها اعداد پذیرفته میشوند')
    title           = models.CharField(max_length=255, unique=True, primary_key=True)
    description     = models.TextField()
    thumbnail       = models.ImageField(upload_to='product/')
    price           = models.DecimalField(max_digits=12, decimal_places=2)
    old_price       = models.DecimalField(max_digits=12, decimal_places=2)
    barcode         = models.CharField(max_length=15, validators=[numbers])
    active          = models.BooleanField(default=True)
    created_at      = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
    
    def gallery(self):
        return Gallery.objects.filter(product=self)
    
    def feature(self):
        return Feature.objects.filter(product=self)
    
    class Meta:
        managed = True
        ordering = ['-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title   = models.CharField(max_length = 256)
    img     = models.ImageField(upload_to='gallery/')
    active  = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = True
        ordering = ['title']
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'


class Feature(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    title       = models.CharField(max_length = 256)
    description = models.TextField()
    active      = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = True
        ordering = ['title']
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'


######################################## Cart section ########################################
