from django.contrib import admin
from .models import(
    Main_page,
    Service,
    Blog,
    Contact,
)

admin.site.register(Main_page)
admin.site.register(Service)
admin.site.register(Blog)
admin.site.register(Contact)