from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    caption= models.CharField(max_length=255)
    # image = models.ImageField(upload_to='products/categories', default=None, null=True, )

    class Meta:
        verbose_name = '1. Category'

    def __str__(self):
        return self.title

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)

    class Meta:
        verbose_name = '2. SubCategory'

    def __str__(self):
        return self.title

class Type(models.Model):
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)

    class Meta:
        verbose_name = '3. Type'

    def __str__(self):
        return self.title
    
    # def __str__(self):
    #     return f'{self.subcategory.category}-{self.subcategory}-{self.title}'

class Brand(models.Model):
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)

    class Meta:
        verbose_name = '4. Brand'

    def __str__(self):
        return self.title





class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products')
    discount = models.FloatField(default=0)
    status = models.BooleanField(default=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    features = models.TextField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    specification = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = '5. Product'

    def __str__(self):
        return self.name

