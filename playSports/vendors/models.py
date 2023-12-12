from django.db import models
from accounts.models import User, UserProfile
import uuid


po_status = [('pending','pending'),('completed','completed'),('canceled','canceled')]


# Create your models here.
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='userprofile')
    name = models.CharField(max_length=50)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True, default=uuid.uuid4, editable=False)
    on_time_delivery_rate = models.FloatField(blank=True,null=True)
    quality_rating_avg = models.FloatField(blank=True,null=True)
    average_response_time = models.FloatField(blank=True,null=True) 
    fulfillment_rate = models.FloatField(blank=True,null=True)
    

class Order(models.Model):
    po_number = models.CharField(max_length=50, unique=True, default=uuid.uuid4, editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True, blank=True)
    delivery_date = models.DateTimeField(blank=True,null=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=po_status, default='pending')
    quality_rating = models.FloatField(blank=True,null=True)
    issue_date = models.DateTimeField(auto_now_add=True,blank=True)
    acknowledgment_date = models.DateTimeField(null=True,blank=True)

# Historical model  
class VendorPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()