from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UserModelSerializer
from .models import User, UserProfile
from rest_framework.response import Response
from rest_framework import status
from vendors.serializers import VendorModelSerializer
from vendors.models import Vendor
# Create your views here.

@api_view(http_method_names=['post'])
def userRegister(request):
    if request.method == 'POST':
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            user = serializer.save()
            user.role = User.CUSTOMER
            user.set_password(password)
            user.save()
             
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['post'])
def vendorRegister(request):
    if request.method == 'POST':
        user_serializer = UserModelSerializer(data=request.data)
        
        vendor_serializer = VendorModelSerializer(data=request.data)
        
        if user_serializer.is_valid() and vendor_serializer.is_valid():
            
            user_data = user_serializer.validated_data
            password = user_data.pop('password')

            # Create and save the user
            user = User.objects.create_user(password=password, **user_data)
            user.role = User.VENDOR
            user.save()

            # Create and save the vendor
            vendor_data = vendor_serializer.validated_data
            vendor = Vendor.objects.create(user=user, **vendor_data)
            vendor.userprofile = UserProfile.objects.get(user=user)
            vendor.name = f"{user.first_name} {user.last_name}"
            vendor.vendor_code = f"{user.first_name}{vendor_data['contact_details']}"
            vendor.save()
            return Response(data={'message':'vendor instance created'},status=status.HTTP_201_CREATED)
        return Response(data=user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)