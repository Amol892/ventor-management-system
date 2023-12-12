from rest_framework import serializers
from .models import *

class VendorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['contact_details','address']
        
        
class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        

class VendorPerformanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorPerformance
        fields = '__all__'
        
        
        