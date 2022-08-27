from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('category/', category, name='category'),
    path('sub_cat/<int:sub_id>', sub_category, name='sub_cat'),
    path('products/<int:pro_id>', product, name='product'),
    path('detail/<int:det_id>', detail, name='detail'),
    path('sub/get/<int:id>', sub_get_api, name='sub_get_api'),
    path('sub/api/', sub_list_api, name='sub_list_api'),

]
