from django.urls import path
from django.contrib import admin

from . import views

app_name = 'payment'

urlpatterns = [
    path('basket/', views.basket, name='basket'),
    path('shipping/', views.shipping, name='shipping'),
    path('razorpay/', views.homepage, name='homepage'),
    path('razorpay/paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('admin/', admin.site.urls),
]

# path('', views.BasketView, name='basket'),
# path('pay/', views.initiate_payment, name='pay'),
# path('callback/', views.callback, name='callback'),
# path('razorpay/', views.homepage, name='index'),
