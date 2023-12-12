from django.shortcuts import render
from .serializers import *
from accounts.serializers import UserModelSerializer
from .models import *
from accounts.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class vendorRegister(APIView):
    
    def post(self,request):
        
        user_serializer = UserModelSerializer(data=request.data)
        
        vendor_serializer = VendorModelSerializer(data=request.data)
        
        if user_serializer.is_valid() and vendor_serializer.is_valid():
            
            user_data = user_serializer.validated_data
            password = user_data.pop('password')

            # Create and save the user
            user = User.objects.create_user(password=password, **user_data)
            user.role = User.VENDOR
            user.save()
            print(user)
            # Create and save the vendor
            print('userprofile',UserProfile.objects.get(user=user))
            vendor_data = vendor_serializer.validated_data
            vendor_code = f"{user.first_name[:2]}{vendor_data['contact_details'][:5]}"
            contact_details = vendor_data['contact_details']
            address = vendor_data['address']
            vendor = Vendor.objects.create(user=user,userprofile=UserProfile.objects.get(user=user), vendor_code = vendor_code, contact_details=contact_details,address=address)
            vendor.name = f"{user.first_name} {user.last_name}" 
            vendor.save()
            
            return Response(data={'message':'vendor instance created'},status=status.HTTP_201_CREATED)
        return Response(data=user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
