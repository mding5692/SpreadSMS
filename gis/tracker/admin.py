from django.contrib import admin
from tracker.models import Person, Object, Contact


class EntityAdmin(admin.ModelAdmin):
    list_display = ('date', 'person_id', 'x', 'y', 'z')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('time', 'a', 'b')

admin.site.register(Person)
admin.site.register(Object, EntityAdmin)
admin.site.register(Contact, ContactAdmin)