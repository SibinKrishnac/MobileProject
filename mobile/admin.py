from django.contrib import admin

# Register your models here.
from .models import Mobile,Brands,Orders
admin.site.register(Mobile)
admin.site.register(Brands)
admin.site.register(Orders)
