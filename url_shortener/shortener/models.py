from django.db import models


class Domain(models.Model):
    name = models.CharField(
        max_length=200, unique=True, verbose_name="Domain name"
    )
    blocked = models.BooleanField(verbose_name="Is blocked")

    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains"
        ordering = ["name"]

    def __str__(self):
        return f"Domain {self.name}"


class URL(models.Model):
    url_original = models.URLField(
        max_length=200, verbose_name="Full url", unique=True
    )
    url_short = models.CharField(
        max_length=10, verbose_name="Short url", unique=True
    )
    domain = models.ForeignKey(
        Domain,
        on_delete=models.CASCADE,
        related_name="urls",
        verbose_name="domain",
    )
    blocked = models.BooleanField(verbose_name="Is blocked")

    class Meta:
        verbose_name = "URL"
        verbose_name_plural = "URLs"
        ordering = ["url_short"]

    def __str__(self):
        return f"{self.url_original} - {self.url_short}"
