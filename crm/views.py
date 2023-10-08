from django.shortcuts import render
from .models import Order
from .forms import OrderForm


def first_page(request):
    object_list = Order.objects.all()
    form = OrderForm()
    return render(request, './index.html', {'object_list': object_list,
                                            'form': form})
