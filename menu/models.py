from django.db import models
from users.models import CustomUser

# Create your models here.

class MenuCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name

class MenuProducts(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

class MenuOrder(models.Model):
    PAYMENT_ONLINE = 'Online'
    PAYMENT_OFFLINE = 'Offline'

    PAYMENT_CHOICES = (
        (PAYMENT_ONLINE, 'Online'),
        (PAYMENT_OFFLINE, 'Offline'),
    )


    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(MenuProducts, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=20,
                                      choices=PAYMENT_CHOICES,
                                      default=PAYMENT_ONLINE)

    def __str__(self):
        return self.user.username + '-' + self.product.name
