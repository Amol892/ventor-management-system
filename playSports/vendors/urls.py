from rest_framework.urls import path
from .views import *


urlpatterns = [
    path('vendorregister/',vendorRegister.as_view())
]
