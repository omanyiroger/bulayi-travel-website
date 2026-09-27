from types import SimpleNamespace

from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class BulayiSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return [
            "home",
            "destinations",
            "dubai",
            "zanzibar",
            "paris",
            "guangzhou",
            "nairobi",
            "eldoret",
            "mombasa",
            "kisumu",
            "nakuru",
        ]

    def location(self, item):
        return reverse(item)

    def get_urls(self, page=1, site=None, protocol=None):
        bulayi_site = SimpleNamespace(domain="bulayitravel.com")
        return super().get_urls(
            page=page,
            site=bulayi_site,
            protocol="https",
        )
