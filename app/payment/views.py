from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from orders.views import add_order, payment_confirmation, billing_address
from basket.basket import Basket
import razorpay
from django.http import HttpResponseBadRequest

razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def basket(request):
    return render(request, 'store/payment/summary.html')


def shipping(request):
    return render(request, 'store/payment/shipping.html')


@login_required
def homepage(request):
    currency = 'INR'
    basket = Basket(request)
    total = str(basket.get_total_price())
    total1 = total.replace('.', '')
    amount = int(total1)


    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
    print(razorpay_order)


    razorpay_order_id = razorpay_order['id']
    razorpay_order_status = razorpay_order['status']
    callback_url = 'paymenthandler/'
    try:
        add_order(razorpay_order, request)
    except Exception as e:
        print(e)
    try:
        billing_address(request,razorpay_order['id'])
    except Exception as ex:
        print(ex)

    context = {'razorpay_order_id': razorpay_order_id,
               'razorpay_order_status': razorpay_order_status,
               'razorpay_merchant_key': settings.RAZOR_KEY_ID,
               'razorpay_amount': amount,
               'currency': currency,
               'callback_url': callback_url,
               'basket':basket,
               'amount': total,
               }
    return render(request, 'store/payment/final_pay.html', context=context)


@csrf_exempt
def success(request):
    return render(request, "success.html")


@csrf_exempt
def paymenthandler(request):
    check_basket = Basket(request)
    total = str(check_basket.get_total_price())
    total = total.replace('.', '')
    check_amount = int(total)

    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature,
            }

            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is True:
                try:
                    razorpay_client.payment.capture(payment_id, check_amount)
                    # Save this order to database here note by onkar
                    payment_confirmation(razorpay_order_id, )
                    check_basket.clear()
                    return render(request, 'store/payment/payment_successfull.html')
                except:
                    return render(request, 'store/payment/payment_fail.html')
            else:
                return render(request, 'store/payment/payment_fail.html')
        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()
