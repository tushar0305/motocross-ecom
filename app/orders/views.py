from django.http.response import JsonResponse

from account.models import UserBase
from basket.basket import Basket
from .models import Order, OrderItem


def add_order(razorpay_order, request):
    basket = Basket(request)
    user_id = request.user.id
    user_data = UserBase.objects.filter(id=user_id).values()

    order_key = razorpay_order['id']
    amount = razorpay_order['amount'] / 100
    order = Order.objects.create(user_id=user_id,
                                 order_key=order_key,
                                 total_amount=amount,
                                 )
    order_id = order.pk
    for item in basket:
        OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'],
                                 quantity=item['qty'])


def payment_confirmation(order_key):
    Order.objects.filter(order_key=order_key).update(billing_status=True)


def billing_address(request, key):
    name = request.POST.get("custName", '')
    address = request.POST.get("custAdd", '')
    phone = request.POST.get("phone", '')
    Order.objects.filter(order_key=key).update(full_name=name, address=address, phone=phone)

def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        order_key = request.POST.get('order_key')
        user_id = request.user.id
        baskettotal = basket.get_total_price()

        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(user_id=user_id, full_name='name', address1='add1',
                                         address2='add2', total_paid=baskettotal, order_key=order_key)
            order_id = order.pk

            for item in basket:
                OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'],
                                         quantity=item['qty'])

        response = JsonResponse({'success': 'Return something'})
        return response


"""# updates status in models file
def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)"""


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders
