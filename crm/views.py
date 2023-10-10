from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from slider.models import SliderContent

def first_page(request):
    # object_list = Order.objects.all()
    # form = OrderForm()
    slider_list = SliderContent.objects.all()

    return render(request, './index.html', {'slider_list': slider_list
                                            })


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    new_user = Order(order_name=name, order_phone=phone)
    new_user.save()
    return render(request, './thanks.html', {'name': name})
