from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_ROLES = (
        ('customer', 'Customer'),
        ('delivery_boy', 'Delivery Boy'),
        ('seller', 'Seller'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=USER_ROLES)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)  # For delivery boy
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # For delivery boy

class FoodRequest(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='food_requests')
    description = models.TextField()  # What food to share
    contact_number = models.CharField(max_length=15)
    status = models.CharField(max_length=20, default='pending')
    delivery_boy = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL, related_name='deliveries')

class SellerItem(models.Model):
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='items/', null=True, blank=True)
