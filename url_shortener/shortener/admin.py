from django.contrib import admin

from shortener.models import URL, Domain

admin.site.register(Domain)
admin.site.register(URL)
