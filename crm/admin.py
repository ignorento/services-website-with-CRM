from django.contrib import admin
from crm.models import Order, StatusCrm, CommentCrm

# Register your models here.
admin.site.register(Order)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
