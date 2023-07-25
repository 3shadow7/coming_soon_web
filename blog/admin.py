from django.contrib import admin
from .models import Subscriber , contact



class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'date_subscribed',)

class contactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name' , 'email', 'date_submitted',)


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(contact, contactAdmin)
