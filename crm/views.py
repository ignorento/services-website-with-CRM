from django.shortcuts import render
from .models import Order
from .forms import OrderForm


def first_page(request):
    object_list = Order.objects.all()
    form = OrderForm()
    return render(request, './index.html', {'object_list': object_list,
                                            'form': form})


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    new_user = Order(order_name=name, order_phone=phone)
    new_user.save()
    return render(request, './thanks.html', {'name': name})
