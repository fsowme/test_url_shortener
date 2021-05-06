from django.contrib import admin

from shortener.models import URL, Domain


class DomainAdmin(admin.ModelAdmin):
    list_display = ("name", "blocked")


class URLAdmin(admin.ModelAdmin):
    list_display = (
        "url_original",
        "url_short",
        "domain",
        "blocked",
        "domain_blocked",
    )

    def domain(self, obj):
        return obj.domain.name

    def domain_blocked(self, obj):
        return obj.domain.blocked


admin.site.register(Domain, DomainAdmin)
admin.site.register(URL, URLAdmin)
