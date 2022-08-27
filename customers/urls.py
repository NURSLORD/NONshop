from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

import customers
from customers.views import register, login_own, test_auth, logout
from product.views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_own, name='my_login'),
    path('test/', test_auth, name='test'),
    path('logout/', logout, name='logout_my'),
    path('', include('django.contrib.auth.urls')),
]
