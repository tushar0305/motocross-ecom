from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('products/', views.total_products, name='total_products'),
    path('item/<id>/', views.detail_product, name='detail_product'),
    path('item/<slug:bike_slug>/', views.detail_product, name='bikes_list'),
]
