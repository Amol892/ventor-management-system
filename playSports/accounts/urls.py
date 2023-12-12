from rest_framework.urls import path
from .views import userRegister

urlpatterns = [
    path('userregister/',userRegister)
]