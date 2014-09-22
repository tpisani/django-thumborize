import re

from collections import Iterable

from libthumbor import CryptoURL

from thumborize import conf

crypto = CryptoURL(key=conf.THUMBOR_SECURITY_KEY)

filter_pattern = re.compile("(?P<name>\w+)(?P<param>\(.*\))")


class ThumborURL(object):
    """
    Manages arguments and options of thumbor URLs.
    """

    def __init__(self, image_url, **options):
        filters = options.pop("filters", {})
        self.image_url = image_url
        self.options = options
        self.filters = self._parse_filters(filters)
        self._merge_filters()

    def _merge_filters(self):
        defaults = conf.THUMBOR_DEFAULT_FILTERS.copy()
        defaults.update(self.filters)
        self.filters = defaults

    def _filters_dict(self, filters):
        filters_dict = {}
        for item in filters:
            sre = filter_pattern.match(item)
            name, param = sre.groups()
            filters_dict[name] = param
        return filters_dict

    def _parse_filters(self, filters):
        if isinstance(filters, basestring):
            return self._filters_dict(filters.split(":"))
        elif isinstance(filters, Iterable):
            return self._filters_dict(filters)
        elif isinstance(filters, dict):
            return filters
        else:
            raise TypeError("Filters must be either a string, iterable or dict.")

    @property
    def filter_list(self):
        return ["{k}{v}".format(k=key, v=value) for key, value in self.filters.items()]

    def generate(self):
        options = self.options.copy()
        options["filters"] = self.filter_list
        encrypted = crypto.generate(image_url=self.image_url, **options)
        return conf.THUMBOR_SERVER + encrypted


def url(image_url, **options):
    """
    Small shortcut for generating URLs by ThumborURL.
    """
    thumbor = ThumborURL(image_url, **options)
    return thumbor.generate()
