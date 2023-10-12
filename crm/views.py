from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from slider.models import SliderContent
from price.models import PriceTable, PriceCard


def first_page(request):
    # object_list = Order.objects.all()
    slider_list = SliderContent.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {'slider_list': slider_list,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'price_table': price_table,
                'form': form,
                }
    return render(request, './index.html', dict_obj)


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    new_user = Order(order_name=name, order_phone=phone)
    new_user.save()
    return render(request, './thanks.html', {'name': name})
