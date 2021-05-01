import json
import random
import string
from json import JSONDecodeError
from urllib.parse import urlparse

from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect

from shortener.models import URL, Domain


def get_short_url(request, short_path):
    if request.method != "GET":
        return HttpResponse("Invalid method")
    try:
        url = URL.objects.get(url_short=short_path)
    except ObjectDoesNotExist:
        return HttpResponse("There is no such address")
    if url.blocked or url.domain.blocked:
        return HttpResponse("URL or domain in blacklist")
    return redirect(url.url_original)


def make_short_url(request):
    if request.method != "POST":
        return HttpResponse("Invalid method")
    try:
        data = json.loads(request.body.decode("utf-8"))
    except TypeError:
        return HttpResponse("Must be a json")
    except JSONDecodeError:
        return HttpResponse("Wrong JSON format")
    if not data.get("url"):
        return HttpResponse("The request must contain url")
    new_url = data["url"]
    if not urlparse(new_url).scheme:
        return HttpResponse("Address must contain 'scheme'")
    domain_name = urlparse(new_url).netloc
    domain, _ = Domain.objects.get_or_create(
        name=domain_name, defaults={"blocked": False}
    )
    if domain.blocked:
        return JsonResponse({"url": "domain in blacklist"})
    # Адреса не сильно уникальны, вариант только для тестового.
    short_path = "".join(random.choices(string.ascii_letters, k=6))
    url, _ = URL.objects.get_or_create(
        url_original=new_url,
        defaults={"url_short": short_path, "domain": domain, "blocked": False},
    )
    if url.blocked:
        return JsonResponse({"url": "url in blacklist"})
    self_url = request.build_absolute_uri()
    return JsonResponse({"url": self_url + url.url_short})
