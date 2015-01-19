from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100, \
                                     null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        unique_together = ('title', 'slug')
    
    def get_price(self):
        return self.price
    
    def get_absolute_url(self):
        # single_product is the name of the view defined in url.py
        return reverse('single_product', kwargs={"slug": self.slug})
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='products/images/')
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    thumbnail = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.product.title